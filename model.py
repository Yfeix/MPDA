import pandas as pd
import numpy as np
from docx import Document
import os
import gensim
from keras.metrics import Precision, Recall
from keras.layers import Activation, Dense, Dropout, Input, GRU, LSTM, Reshape, Flatten, Conv2D, MaxPooling2D, Bidirectional, RepeatVector, Permute, Multiply, Lambda, LeakyReLU, BatchNormalization, GlobalMaxPooling1D
from keras.models import Model as Models
from Transformer_Encoder import TransformerEncoder  # custom model
from tensorflow.keras.optimizers import RMSprop
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from constants import *
import keras.backend as K
from data_augmentation import *
import tensorflow as tf
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from keras.callbacks import ModelCheckpoint
from data_augmentation import *


# This file is the models implementation for the mpda_compare.py and train_compare.py file calls.

# Allocate GPU memory on demand
gpu_options = tf.compat.v1.GPUOptions(allow_growth=True)
sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(gpu_options=gpu_options))

class Model:
    @staticmethod
    def LSTM():
        inputs = Input(name='inputs', shape=(MAX_LEN, INPUT_SIZE))
        layer = LSTM(64)(inputs)
        layer = Dense(256, name='FC1')(layer)
        layer = Activation(ACTIVATION_FUNCT)(layer)
        layer = Dropout(DROPOUT_RATE)(layer)
        layer = Dense(1, name='out_layer')(layer)
        layer = Activation('sigmoid')(layer)
        model = Models(inputs=inputs, outputs=layer)
        return model

    @staticmethod
    def GRU():
        inputs = Input(name='inputs', shape=(MAX_LEN, INPUT_SIZE))
        layer = GRU(units=64, return_sequences=False)(inputs)
        layer = Dropout(DROPOUT_RATE)(layer)
        layer = Dense(units=256, activation=ACTIVATION_FUNCT)(layer)
        layer = Dropout(DROPOUT_RATE)(layer)
        layer = Dense(units=1, activation='sigmoid', name='out_layer')(layer)
        model = Models(inputs=inputs, outputs=layer)
        return model

    @staticmethod
    def BiLSTM():
        inputs = Input(name='inputs', shape=(MAX_LEN, INPUT_SIZE))
        layer = Bidirectional(LSTM(64))(inputs)
        layer = Dense(256, name='FC1')(layer)
        layer = Activation(ACTIVATION_FUNCT)(layer)
        layer = Dropout(DROPOUT_RATE)(layer)
        layer = Dense(1, name='out_layer')(layer)
        layer = Activation('sigmoid')(layer)
        model = Models(inputs=inputs, outputs=layer)
        return model


    @staticmethod
    def BiGRU():
        inputs = Input(name='inputs', shape=(MAX_LEN, INPUT_SIZE))
        layer = Bidirectional(GRU(64))(inputs)
        layer = Dense(256, name='FC1')(layer)
        layer = Activation(ACTIVATION_FUNCT)(layer)
        layer = Dropout(DROPOUT_RATE)(layer)
        layer = Dense(1, name='out_layer')(layer)
        layer = Activation('sigmoid')(layer)
        model = Models(inputs=inputs, outputs=layer)
        return model
    
    @staticmethod
    def BiGRU_ATT():
        inputs = Input(name='inputs', shape=(MAX_LEN, INPUT_SIZE))
        layer = Bidirectional(GRU(64, return_sequences=True))(inputs)

        # Attention mechanism
        attention = Dense(1, activation='tanh')(layer)
        attention = Flatten()(attention)
        attention = Activation('softmax')(attention)
        attention = RepeatVector(128)(attention)
        attention = Permute([2, 1])(attention)
        sent_representation = Multiply()([layer, attention])
        sent_representation = Lambda(lambda xin: K.sum(xin, axis=-2), output_shape=(128,))(sent_representation)
 
        layer = Dense(256, name='FC1')(sent_representation)
        layer = Activation(ACTIVATION_FUNCT)(layer)
        layer = Dropout(DROPOUT_RATE)(layer)
        layer = Dense(1, name='out_layer')(layer)
        layer = Activation('sigmoid')(layer)
        model = Models(inputs=inputs, outputs=layer)
        return model
    
    @staticmethod
    def Transformer():
        inputs = Input(name='inputs', shape=(MAX_LEN, INPUT_SIZE))
        layer = TransformerEncoder(embed_dim=INPUT_SIZE, dense_dim=INPUT_SIZE*4,num_heads=8)(inputs)
        layer = GlobalMaxPooling1D()(layer)
        layer = Dense(256, name='FC1')(layer)
        layer = Activation(ACTIVATION_FUNCT)(layer)
        layer = Dropout(DROPOUT_RATE)(layer)
        layer = Dense(1, name='out_layer')(layer)
        layer = Activation('sigmoid')(layer)
        model = Models(inputs=inputs, outputs=layer)
        return model
    

    @staticmethod
    def f1_score1(y_true, y_pred):
        # Calculate Precision and Recall metrics.
        TP = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        FP = K.sum(K.round(K.clip(y_pred - y_true, 0, 1)))
        FN = K.sum(K.round(K.clip(y_true - y_pred, 0, 1)))

        precision = TP / (TP + FP + K.epsilon())
        recall = TP / (TP + FN + K.epsilon())

        # Calculate F1-Score
        f1_score = 2 * precision * recall / (precision + recall + K.epsilon())

        return f1_score
    

    @staticmethod
    def train(cwe_name, net, t_type, i, X_train_all, Y_train_all, X_val, Y_val, X_test, Y_test, length):
        i = str(i)
        vul_type = cwe_name.split("_")[0]

        # model & train
        if net == "lstm":
            netModel = Model.LSTM()
        elif net == "gru":
            netModel = Model.GRU()
        elif net == "bilstm":
            netModel = Model.BiLSTM()
        elif net == "bigru":
            netModel = Model.BiGRU()
        elif net == "bigru_att":
            netModel = Model.BiGRU_ATT()
        elif net == "transformer":
            netModel = Model.Transformer()
        elif net == "cnn":
            netModel = Model.CNN()
        else:
            print("net is wrong")
            return     

        if net == "lstm" or  net == "gru" or net == "bilstm" or net == "bigru" or net == "bilstm_att" or net == "bigru_att" or net == "transformer" or net == "cnn":
            
            checkpoint = ModelCheckpoint('Net_best/' + net + vul_type + i + '_best_model.h5', monitor='val_loss', save_best_only=True, mode='min', verbose=1)
            netModel.summary()
            netModel.compile(loss=LOSS_FUNCT, optimizer=RMSprop(), metrics=['accuracy', Precision(), Recall(), Model.f1_score1])
            netModel.fit(X_train_all, Y_train_all, batch_size=BATCH_SIZE_NET, epochs=EPOCH_NET, validation_data=(X_val, Y_val), callbacks=[checkpoint])
            netModel.save('Net/' + net + vul_type + i + '_model.h5', overwrite=True)
            netModel = load_model('Net/' + net + vul_type + i + '_model.h5', custom_objects = {"TransformerEncoder": TransformerEncoder}, compile=False)
            netModel.compile(loss=LOSS_FUNCT, optimizer=RMSprop(), metrics=['accuracy', Precision(), Recall(), Model.f1_score1])
            accr = netModel.evaluate(X_test, Y_test)

            print('{} Test set\n  Loss: {:0.3f}\n  Accuracy: {:0.3f}\n  Precision: {:0.3f}\n  Recall: {:0.3f}\n  F1Score: {:0.3f}\n'.format(cwe_name, accr[0], accr[1], accr[2], accr[3], accr[4]))

            filename = 'result/'+ t_type + net + '.csv'
           
            new_data = {'CWE-name': cwe_name, 'Loss': accr[0], 'Accuracy': accr[1], 'Precision': accr[2], 'Recall': accr[3], 'F1Score': accr[4], 'length': length}

            # If the file does not exist, create a new file and write the new data
            if not os.path.isfile(filename):
                df = pd.DataFrame(columns=['CWE-name', 'Loss', 'Accuracy', 'Precision', 'Recall', 'F1Score', 'length'])
                df.loc[0] = [new_data['CWE-name'], new_data['Loss'], new_data['Accuracy'], new_data['Precision'], new_data['Recall'], new_data['F1Score'], new_data['length']]
                # df = pd.DataFrame(new_data, index=[0])
                df.to_csv(filename, index=False, float_format='%.3f')
            else:
                # Otherwise read the original data file and append the new data below the corresponding CWE-name.
                df = pd.read_csv(filename)
                grouped_df = df.groupby('CWE-name')
                if new_data['CWE-name'] in grouped_df.groups:
                    # If the same CWE-name exists, add the new data to the bottom of the group
                    group = grouped_df.get_group(new_data['CWE-name'])
                    new_index = group.index[-1] + 1
                    if new_index < len(df):
                        new_row = pd.DataFrame([new_data], columns=df.columns)
                        df = pd.concat([df.iloc[:new_index], new_row, df.iloc[new_index:]], ignore_index=True)

                    df.loc[new_index] = [new_data['CWE-name'], new_data['Loss'], new_data['Accuracy'], new_data['Precision'], new_data['Recall'], new_data['F1Score'], new_data['length']]
                else:
                    # Otherwise, add new data at the bottom of the data
                    new_index = len(df)
                    df.loc[new_index] = [new_data['CWE-name'], new_data['Loss'], new_data['Accuracy'], new_data['Precision'], new_data['Recall'], new_data['F1Score'], new_data['length']]
                df.to_csv(filename, index=False, float_format='%.3f')



