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

# This file is to compare the performace of augmented data and raw data in the same data size. 
# Import this file and call the train() method at the end of the preprocessing.py file.

def train(df, cwe_name, net, t_type, i):
        # cwe_name = os.path.basename(write_h5_to).split(".h5")[0]
        # length = len(df)
        vul_type = cwe_name.split("_")[0]

        if isinstance(df, str):
            df = pd.read_csv(df)
            print(df)

        if net == "lstm" or net == "gru" or net == "cnn":
            net_type = "basic"
        elif net == "bilstm" or net == "bigru" or net == "bigru_att":
            net_type = "advanced"
        else:
            print("the net is wrong!!")
            return

        
        X_train, Y_train, X_val, Y_val, X_test, Y_test = embedding.emb_word2vec(df)

        num_samples = len(X_train) // 3

        indices_o = np.random.choice(len(X_train), size=num_samples, replace=False)
        X_sampled = X_train[indices_o]
        Y_sampled = Y_train[indices_o]

        print(len(X_sampled))
        print(len(X_train))

        Model.train(cwe_name, net, 'raw1', i, X_sampled, Y_sampled, X_val, Y_val, X_test, Y_test, len(X_sampled))
        Model.train(cwe_name, net, 'raw2', i, X_train,  Y_train, X_val, Y_val, X_test, Y_test, len(X_train))



        X_train_all, Y_train_all = Data_augmentation.data_augmentation(X_train, Y_train, vul_type, net_type, net)
        
        indices_a1 = np.random.choice(len(X_train_all), size=num_samples, replace=False)
        X_a1_sampled = X_train_all[indices_a1]
        Y_a1_sampled = Y_train_all[indices_a1]

        indices_a2 = np.random.choice(len(X_train_all), len(X_train), replace=False)
        X_a2_sampled = X_train_all[indices_a2]
        Y_a2_sampled = Y_train_all[indices_a2]

        X_train_all, Y_train_all = None, None

        print(len(X_a1_sampled))
        print(len(X_a2_sampled))

        Model.train(cwe_name, net, 'aug1', i, X_a1_sampled, Y_a1_sampled, X_val, Y_val, X_test, Y_test, len(X_a1_sampled))
        Model.train(cwe_name, net, 'aug2', i, X_a2_sampled, Y_a2_sampled, X_val, Y_val, X_test, Y_test, len(X_a2_sampled))



        



