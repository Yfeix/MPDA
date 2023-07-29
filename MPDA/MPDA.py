import argparse
import os
from constants import *
from preprocessing import Preprocessing
from result_processing import *


def main():
    # Top-level parser.
    parser = argparse.ArgumentParser(prog='MPDA')
    subparsers = parser.add_subparsers(help='sub-command help')

    # MPDA train folder 30 net    =>    directory='folder', 'threshold=30', net='lstm'
    train = subparsers.add_parser('train', help='train models on class files in a given directory')
    train.add_argument('directory', type=str, help='path to a folder containing corpus classes')
    train.add_argument('threshold', type=int, help='drop vulnerability classes with fewer example'
                                                   ' classes than the given threshold.')
    train.add_argument('net', type=str, help='the net type is written in')

    args = str(parser.parse_args())[10:-1]

    if "directory=" in args:  # train
        directory, threshold, net = args.replace("directory=", "").replace("threshold=", "")\
                                             .replace("net=", "").replace("\'", "").split(", ")

        if os.path.isdir(directory):
            print("\x1b[33mTraining vulnerability models using files from \"" +
                      directory + "\" with a threshold of " + threshold + " and the net choose " + net + ".\x1b[m")
            Preprocessing.train_models(directory, (int)(threshold), net)

            result_processing("result/" + net +"_result.csv")
        else:
            print("\x1b[31mUnable to locate folder: " + directory + "\x1b[m")


if __name__ == "__main__":
    main()
