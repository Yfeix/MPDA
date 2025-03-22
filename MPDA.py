import argparse
import os
from constants import *
from preprocessing import Preprocessing
import time

def main():
    # Top-level parser.
    parser = argparse.ArgumentParser(prog='MPDA')
    subparsers = parser.add_subparsers(help='sub-command help')

    # MPDA train folder 30 net    =>    directory='folder', 'threshold=30', net='lstm'
    train = subparsers.add_parser('train', help='train models on class files in a given directory')
    train.add_argument('directory', type=str, help='path to a folder containing corpus classes')
    # train.add_argument('net', type=str, help='the net type is written in')
    # train.add_argument('t_type', type=str, help='the type is written in')
    train.add_argument('threshold', type=int, help='drop vulnerability classes with fewer example'
                                                   ' classes than the given threshold.')
    

    args = str(parser.parse_args())[10:-1]

    if "directory=" in args:  # train
        # directory, net, t_type, threshold = args.replace("directory=", "").replace("net=", "").replace("t_type=", "")\
        #                                      .replace("threshold=", "").replace("\'", "").split(", ")

        directory, threshold = args.replace("directory=", "").replace("threshold=", "").replace("\'", "").split(", ")

        if os.path.isdir(directory):
            print("\x1b[33mTraining vulnerability models using files from \"" + directory + "\" with a threshold of " + threshold +".\x1b[m")
            
            # The following annotated codes (from line 35 to line 52) are for statistical code representation experiments.
            # time_list = []
            for i in range(10): # The integer data in range() is the number of cyclic experiments.
                # start_time = time.time()
                Preprocessing.train_models(directory, (int)(threshold), i)
                # end_time = time.time()
                # execution_time = end_time - start_time
                # time_list.append(execution_time)
                # print(f"Time of the {i+1}th execution: {execution_time} sec")
        else:
            print("\x1b[31mUnable to locate folder: " + directory + "\x1b[m")
        
        # print(time_list)
        # average = sum(time_list) / len(time_list)
        # print(f"Average time: {average} sec")
        # with open('emb_test/'+t_type+'.txt', 'a+', encoding='utf-8') as file:
        #     file.write(str(time_list))
        #     file.write("\n")
        #     file.write(f"Average time: {average} sec\n")


if __name__ == "__main__":
    main()
    # Run the following command in a terminal
    # python MPDA.py train "./data/cwe" 100