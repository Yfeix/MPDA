import javalang
import re
import numpy as np
import random
import string

## For comparing diffenent model with mpda. It can also train the model with MPDA.
from mpda_compare import *

## For comparing augmented data and original data.
# from train_compare import *


# JavaClass: receives a `path` of a Java file, extracts the code, converts the code from Allman to K&R, 
# extracts the methods, and creates a list of JavaMethod objects.
class JavaClass:
    def __init__(self, path):
        self.src = JavaClass._extract_code(path)
        self.src = JavaClass._allman_to_knr(self.src)
        self.methods = JavaClass.chunker(self.src)
        self.method_names = [method.name for method in self.methods]

    # __iter__: iterate through the methods in the JavaClass.
    def __iter__(self):
        return iter(self.methods)

    # _extract_code: receives a `path` to a Java file, removes all comments, and returns the contents of the file sans comments.
    @staticmethod
    def _extract_code(path):
        with open(path, 'r') as content_file:
            contents = content_file.read()
            contents = re.sub(re.compile("/\*.*?\*/", re.DOTALL), "", contents)
            contents = re.sub(re.compile("//.*?\n"),  "", contents)
            return contents

    # tokens: A getter that returns a 1-dimensional space-delimited string of tokens for the whole source file.
    def tokens(self):
        tokens = javalang.tokenizer.tokenize(self.src)
        return [" ".join(token.value for token in tokens)][0]

    # find_occurences: Returns a list of all occurrences of a character `ch` in a string `s`.
    @staticmethod
    def find_occurrences(s, ch):
        return [i for i, letter in enumerate(s) if letter == ch]

    # _allman_to_knr: Converts a string `contents` from the style of allman to K&R. This is required for `chunker` to work correctly.
    @staticmethod
    def _allman_to_knr(contents):
        s, contents = [], contents.split("\n")
        line = 0
        while line < len(contents):
            if contents[line].strip() == "{":
                s[-1] = s[-1].rstrip() + " {"
            else:
                s.append(contents[line])
            line += 1
        return "\n".join(s)

    # chunker: Extracts the methods from `contents` and returns a list of `JavaMethod` objects.
    @staticmethod
    def chunker(contents):
        r_brace = JavaClass.find_occurrences(contents, "}")
        l_brace = JavaClass.find_occurrences(contents, "{")
        tokens = javalang.tokenizer.tokenize(contents)
        guide, chunks = "", []
        _blocks = ["enum", "finally", "catch", "do", "else", "for",
                   "if", "try", "while", "switch", "synchronized"]

        for token in tokens:
            if token.value in ["{", "}"]:
                guide += token.value

        while len(guide) > 0:
            i = guide.find("}")
            l, r = l_brace[i - 1], r_brace[0]
            l_brace.remove(l)
            r_brace.remove(r)

            ln = contents[0:l].rfind("\n")
            chunk = contents[ln:r + 1]
            if len(chunk.split()) > 1:
                if chunk.split()[0] in ["public", "private", "protected"] and "class" not in chunk.split()[1]:
                    chunks.append(JavaMethod(chunk))
            guide = guide.replace("{}", "", 1)
        return chunks


# JavaMethod: receives a `chunk`, which is the method string.
class JavaMethod:
    def __init__(self, chunk):
        self.method = chunk
        self.name = chunk[:chunk.find("(")].split()[-1]

    # tokens: a getter that returns a 1-dimensional space-delimited string of tokens for the method.
    def tokens(self):
        tokens = javalang.tokenizer.tokenize(self.method)
        return [" ".join(token.value for token in tokens)][0]

    # __str__: String representation for a method.
    def __str__(self):
        return self.method

    # __iter__: Iterator for the tokens of each method.
    def __iter__(self):
        tokens = javalang.tokenizer.tokenize(self.method)
        return iter([tok.value for tok in tokens])


# CWE4J: receives a path `root` to a folder containing labeled Java classes with known vulnerabilities.
# Each Java file in the `root` directory is then added to a dictionary `data` of the form {vulnerability: [path_1, path_2, ..., path_n]}
class get_cwe:
    def __init__(self, root):
        self.data = {}
        self.root = root
        for directory in os.listdir(root):
            self.add(directory)

    # add: if the vulnerability already has an entry in `self.data`,the filepath will be appended to the value list. 
    # Otherwise, the name of the vulnerability and a list containing the path to the vulnerability are created as the key and value, respectively.
    def add(self, filepath):
        vuln_name = filepath.split("__")[0]
        if vuln_name in self.data.keys():
            self.data[vuln_name].append(self.root + "/" + filepath)
        else:
            self.data[vuln_name] = [self.root + "/" + filepath]

    # __iter__: iterator for the keys of `self.data`.
    def __iter__(self):
        return iter(self.data.keys())

    # __getitem__: allows a get_cwe object to be indexed by key.
    def __getitem__(self, item):
        return self.data[item]

    # __len__: returns the number of keys in `self.data`.
    def __len__(self):
        return len(self.data.keys())


# Preprocessing: contains functions that are responsible for 'MPDA' core functionality.
class Preprocessing:
    # train_models: trains several models from appropriately names Java files from a `root` directory. 
    # The `threshold` will tell MPDA to ignore any vulnerability categories that contain less than a given number of examples to train on.
    @staticmethod
    def train_models(root, threshold, i):
        cwes = get_cwe(root)
        for cwe in cwes:
            if len(cwes[cwe]) >= threshold:
                K.clear_session()
                Preprocessing._train_model(str(cwe), cwes[cwe], i)

    # _train_model: A helper method for `train_models`, that examines the method name of each method in the given training files.
    # If a method name contains the word "bad", it is labeled with a 1; if it contains "good", it is labeled with a 0. 
    # The labeled data is returned in a pandas dataframe of the form [tokenized java method, binary polarity bit (0/1)].
    @staticmethod
    def _train_model(cwe_name, cwe_paths,  i):
        print(cwe_name)
        df = [["input", "label"]]
        for path in cwe_paths:
            try:
                j = JavaClass(path)
                for method in j.methods:
                    focus = method.tokens().split("(", 1)
                    if "good" in focus[0]:
                        rand = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
                        temp = focus[0].replace("good", rand) + "(" + focus[1]
                        df.append([temp, "0"])
                        
                    elif "bad" in focus[0]:
                        rand = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
                        temp = focus[0].replace("bad", rand) + "(" + focus[1]
                        df.append([temp, "1"])
        
            except:
                pass
        dataframe = pd.DataFrame(df[1:], columns=df[0])

        train(dataframe, cwe_name, i)   # For mpda_compare.py or train_compare.py

