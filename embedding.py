from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle
import numpy as np
import torch
import torch.nn as nn
import gensim
from transformers import AutoModel, AutoTokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from constants import *
from tqdm import tqdm
from unixcoder import UniXcoder

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# For word2vec using
def get_word_embeddings(model, sentence): 
    words = sentence.split()
    embeddings = [model[word] for word in words if word in model]
    embeddings = np.array(embeddings)
    return embeddings

def emb_word2vec(df):
    X = df.input
    Y = df.label
    le = LabelEncoder()
    Y = le.fit_transform(Y)
    Y = Y.reshape(-1, 1)
    # Word2Vec
    sentences = [[word for word in sentence.split()] for sentence in X]
    model = gensim.models.Word2Vec(sentences, vector_size=INPUT_SIZE, window=5, min_count=1, epochs=20)
    X_emb = [get_word_embeddings(model.wv, sentence) for sentence in X]
    X_emb_padded = pad_sequences(X_emb, maxlen=MAX_LEN, dtype='float32', padding='post', truncating='post')
    
    X_rnn = np.array([vec for vec in X_emb_padded])
    print(X_rnn.shape)

    X_rnn, Y = shuffle(X_rnn, Y)
    # split as 8:1:1
    X_train, X_rest, Y_train, Y_rest = train_test_split(X_rnn, Y, test_size=TEST_SIZE)
    X_val, X_test, Y_val, Y_test = train_test_split(X_rest, Y_rest, test_size=0.5)

    return X_train, Y_train, X_val, Y_val, X_test, Y_test


# It is highly recommended to manually download 
# the pre-training files from huggingface and 
# place them in the 'pretrain_model' directory for local reading.
# Otherwise, you need to modify the “checkpoint” of the following code to the corresponding pre-trained model file name.

def emb_codebert(df):
    inputs = df.input
    labels = df.label
    le = LabelEncoder()
    labels = le.fit_transform(labels)
    labels = labels.reshape(-1, 1)

    checkpoint = "pretrain_model/codebert-base"
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    tokenizer.model_max_length = MAX_LEN
    model = AutoModel.from_pretrained(checkpoint)
    model.to(device)

    code_embeddings = []
    with torch.no_grad():
        for code in tqdm(inputs):
            code_tokens=tokenizer.tokenize(code, truncation=True, padding='max_length')
            tokens=[tokenizer.cls_token]+code_tokens+[tokenizer.eos_token]
            tokens_ids= tokenizer.convert_tokens_to_ids(tokens)
            source_ids= (torch.tensor(tokens_ids)).to(device)
            tokens_embeddings = model(source_ids[None,:])[0][:, 1:-1, :]

            code_embeddings.append(tokens_embeddings[0].cpu().numpy())
    print(np.array(code_embeddings).shape)
    
    inputs_final, labels = shuffle(np.array(code_embeddings), labels)
    # split as 8:1:1
    X_train, X_rest, Y_train, Y_rest = train_test_split(inputs_final, labels, test_size=TEST_SIZE)
    X_val, X_test, Y_val, Y_test = train_test_split(X_rest, Y_rest, test_size=0.5)

    return X_train, Y_train, X_val, Y_val, X_test, Y_test


def emb_graphcodebert(df):
    inputs = df.input
    labels = df.label
    le = LabelEncoder()
    labels = le.fit_transform(labels)
    labels = labels.reshape(-1, 1)

    checkpoint = "pretrain_model/graphcodebert-base"
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    tokenizer.model_max_length = MAX_LEN
    model = AutoModel.from_pretrained(checkpoint)
    model.to(device)

    code_embeddings = []
    with torch.no_grad():
        for code in tqdm(inputs):
            code_tokens=tokenizer.tokenize(code, truncation=True, padding='max_length')
            tokens=[tokenizer.cls_token]+code_tokens+[tokenizer.eos_token]
            tokens_ids= tokenizer.convert_tokens_to_ids(tokens)
            source_ids= (torch.tensor(tokens_ids)).to(device)
            tokens_embeddings = model(source_ids[None,:])[0][:, 1:-1, :]

            code_embeddings.append(tokens_embeddings[0].cpu().numpy())
    print(np.array(code_embeddings).shape)
    
    inputs_final, labels = shuffle(np.array(code_embeddings), labels)
    # split as 8:1:1
    X_train, X_rest, Y_train, Y_rest = train_test_split(inputs_final, labels, test_size=TEST_SIZE)
    X_val, X_test, Y_val, Y_test = train_test_split(X_rest, Y_rest, test_size=0.5)

    return X_train, Y_train, X_val, Y_val, X_test, Y_test


def emb_codet5p(df):
    # If you download the pre-trained model from huggingface, be sure to go to the cache directory and 
    # change the "embedding = F.normalize(self.proj(encoder_outputs.last_hidden_state[:, :, :]), dim=-1)"
    # to "embedding = encoder_outputs.last_hidden_state[:, :, :]" in the modeling_codet5p_embedding.py file.

    # Or you can use the file we provide in pretrain_model/codet5p-110m-embedding/modeling_codet5p_embedding.py

    inputs = df.input
    labels = df.label
    le = LabelEncoder()
    labels = le.fit_transform(labels)
    labels = labels.reshape(-1, 1)

    checkpoint = "pretrain_model/codet5p-110m-embedding"
    tokenizer = AutoTokenizer.from_pretrained(checkpoint, trust_remote_code=True)
    tokenizer.model_max_length = MAX_LEN 
    model = AutoModel.from_pretrained(checkpoint, trust_remote_code=True).to(device)

    code_embeddings = []
    with torch.no_grad():
        for code in tqdm(inputs):
            inputs = tokenizer.encode(code, return_tensors="pt", truncation= True, padding='max_length').to(device)
            code_embedding = model(inputs)[0]
            #print(code_embedding.shape)
            code_embeddings.append(code_embedding.cpu().numpy())

    print(np.array(code_embeddings).shape)
    
    inputs_final, labels = shuffle(np.array(code_embeddings), labels)
    # split as 8:1:1
    X_train, X_rest, Y_train, Y_rest = train_test_split(inputs_final, labels, test_size=TEST_SIZE)
    X_val, X_test, Y_val, Y_test = train_test_split(X_rest, Y_rest, test_size=0.5)

    return X_train, Y_train, X_val, Y_val, X_test, Y_test


def emb_unixcoder(df):
    inputs = df.input
    labels = df.label
    le = LabelEncoder()
    labels = le.fit_transform(labels)
    labels = labels.reshape(-1, 1)

    model = UniXcoder("pretrain_model/unixcoder-base")
    model.to(device)

    code_embeddings = []
    with torch.no_grad():
        for code in tqdm(inputs):
            tokens_ids  = model.tokenize([code], max_length=MAX_LEN,mode="<encoder-only>",padding=True)
            source_ids = torch.tensor(tokens_ids).to(device)
            tokens_embeddings,max_func_embedding = model(source_ids)
            code_embeddings.append(tokens_embeddings[0].cpu().numpy())
    print(np.array(code_embeddings).shape)
    
    inputs_final, labels = shuffle(np.array(code_embeddings), labels)
    # split as 8:1:1
    X_train, X_rest, Y_train, Y_rest = train_test_split(inputs_final, labels, test_size=TEST_SIZE)
    X_val, X_test, Y_val, Y_test = train_test_split(X_rest, Y_rest, test_size=0.5)

    return X_train, Y_train, X_val, Y_val, X_test, Y_test



