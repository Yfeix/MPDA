import pandas as pd
import numpy as np

from constants import *
from data_augmentation import *
import tensorflow as tf
from model import *

import embedding
# Allocate GPU memory on demand
gpu_options = tf.compat.v1.GPUOptions(allow_growth=True)
sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(gpu_options=gpu_options))



def train(df, cwe_name, i):
        # cwe_name = os.path.basename(write_h5_to).split(".h5")[0]
        # length = len(df)
        vul_type = cwe_name.split("_")[0]

        if isinstance(df, str):
            df = pd.read_csv(df)
            print(df)

        net = 'bigru'

        if net == "lstm" or net == "gru" or net == "cnn":
            net_type = "basic"
        elif net == "bilstm" or net == "bigru" or net == "bigru_att" or net == "transformer":
            net_type = "advanced"
        else:
            print("the net is wrong!!")
            return

        
        X_train, Y_train, X_val, Y_val, X_test, Y_test = embedding.emb_word2vec(df)

        X_train_all, Y_train_all = X_train, Y_train

        # If you need to compare the effect of mpda,
        # it is recommended to set up the same training code in the following two places at the same time.

        # The third parameter('base' and 'mpda') is a customized tag, 
        # which will be reflected in the filename of the output result xxx.csv.

        # For training with raw data
        Model.train(cwe_name, 'bigru', 'base', i, X_train_all, Y_train_all, X_val, Y_val, X_test, Y_test, len(Y_train_all))
        # Model.train(cwe_name, 'bilstm', 'base', i, X_train_all, Y_train_all, X_val, Y_val, X_test, Y_test, len(Y_train_all))
        # Model.train(cwe_name, 'transformer', 'base', i, X_train_all, Y_train_all, X_val, Y_val, X_test, Y_test, len(Y_train_all))

        X_train_all, Y_train_all = Data_augmentation.data_augmentation(X_train, Y_train, vul_type, net_type, net)  #MPDA

        # For training with MPDA
        Model.train(cwe_name, 'bigru', 'mpda', i, X_train_all, Y_train_all, X_val, Y_val, X_test, Y_test, len(Y_train_all))
        # Model.train(cwe_name, 'bilstm', 'mpda', i, X_train_all, Y_train_all, X_val, Y_val, X_test, Y_test, len(Y_train_all))
        # Model.train(cwe_name, 'transformer', 'mpda', i, X_train_all, Y_train_all, X_val, Y_val, X_test, Y_test, len(Y_train_all))



        



