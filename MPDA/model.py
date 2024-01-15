import pandas as pd
import numpy as np
import sys
from docx import Document
import os
import csv
import gensim
from keras.metrics import Precision, Recall
from keras.layers import Activation, Dense, Dropout, Input, GRU, Bidirectional, LSTM
from keras.models import Model, load_model
from keras.optimizers import RMSprop
from keras.utils import pad_sequences
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from constants import *
import keras.backend as K
from data_augmentation import *


class MPDAmodel:
    @staticmethod
    def LSTM():
        inputs = Input(name='inputs', shape=(MAX_LEN, 150))
        layer = LSTM(64)(inputs)
        layer = Dense(256, name='FC1')(layer)
        layer = Activation(ACTIVATION_FUNCT)(layer)
        layer = Dropout(DROPOUT_RATE)(layer)
        layer = Dense(1, name='out_layer')(layer)
        layer = Activation('sigmoid')(layer)
        model = Model(inputs=inputs, outputs=layer)
        return model

    @staticmethod
    def GRU():
        inputs = Input(name='inputs', shape=(MAX_LEN, 150))
        layer = GRU(units=64, return_sequences=False)(inputs)
        layer = Dropout(DROPOUT_RATE)(layer)
        layer = Dense(units=256, activation=ACTIVATION_FUNCT)(layer)
        layer = Dropout(DROPOUT_RATE)(layer)
        layer = Dense(units=1, activation='sigmoid', name='out_layer')(layer)
        model = Model(inputs=inputs, outputs=layer)
        return model

    @staticmethod
    def BiLSTM():
        inputs = Input(name='inputs', shape=(MAX_LEN, 150))
        layer = Bidirectional(LSTM(64))(inputs)
        layer = Dense(256, name='FC1')(layer)
        layer = Activation(ACTIVATION_FUNCT)(layer)
        layer = Dropout(DROPOUT_RATE)(layer)
        layer = Dense(1, name='out_layer')(layer)
        layer = Activation('sigmoid')(layer)
        model = Model(inputs=inputs, outputs=layer)
        return model


    @staticmethod
    def BiGRU():
        inputs = Input(name='inputs', shape=(MAX_LEN, 150))
        layer = Bidirectional(GRU(64))(inputs)
        layer = Dense(256, name='FC1')(layer)
        layer = Activation(ACTIVATION_FUNCT)(layer)
        layer = Dropout(DROPOUT_RATE)(layer)
        layer = Dense(1, name='out_layer')(layer)
        layer = Activation('sigmoid')(layer)
        model = Model(inputs=inputs, outputs=layer)
        return model
    

    @staticmethod
    def f1_score(y_true, y_pred):
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
    def get_word_embeddings(model, sentence):

        words = sentence.split()
        embeddings = [model[word] for word in words if word in model]
        embeddings = np.array(embeddings)
        return embeddings

    @staticmethod
    def train(df, write_h5_to, net):
        cwe_name = os.path.basename(write_h5_to).split(".h5")[0]
        length = len(df)
        vul_type = cwe_name.split("_")[0]

        print(write_h5_to)

        if net == "lstm" or net == "gru":
            net_type = "basic"
        elif net == "bilstm" or net == "bigru":
            net_type = "advanced"
        else:
            print("the net is wrong!!")
            return

        if isinstance(df, str):
            df = pd.read_csv(df)
            print(df)

        X = df.input
        Y = df.label
        le = LabelEncoder()
        Y = le.fit_transform(Y)
        Y = Y.reshape(-1, 1)

        # Word2Vec
        sentences = [[word for word in sentence.split()] for sentence in X]
        model = gensim.models.Word2Vec(sentences, vector_size=150, window=5, min_count=1, epochs=20)
        model.wv.save_word2vec_format('word2vec/word2vec_' + vul_type + '.bin', binary=True)
        model = gensim.models.KeyedVectors.load_word2vec_format('word2vec/word2vec_' + vul_type + '.bin', binary=True)

        X_emb = [MPDAmodel.get_word_embeddings(model, sentence) for sentence in X]

        X_emb_padded = pad_sequences(X_emb, maxlen=MAX_LEN, dtype='float32', padding='post', truncating='post')
        X_rnn = np.array([vec for vec in X_emb_padded])

        X_rnn, Y = shuffle(X_rnn, Y)

        X_train, X_rest, Y_train, Y_rest = train_test_split(X_rnn, Y, test_size=TEST_SIZE)
        X_val, X_test, Y_val, Y_test = train_test_split(X_rest, Y_rest, test_size=0.5)

        X_train_all, Y_train_all = Data_augmentation.data_augmentation(X_train, Y_train, vul_type, net_type)

        print(X_train_all.shape)


        # model & train
        if net == "lstm":
            netModel = MPDAmodel.LSTM()
        elif net == "gru":
            netModel = MPDAmodel.GRU()
        elif net == "bilstm":
            netModel = MPDAmodel.BiLSTM()
        elif net == "bigru":
            netModel = MPDAmodel.BiGRU()
        else:
            print("net is wrong")
            return

        netModel.summary()
        netModel.compile(loss=LOSS_FUNCT, optimizer=RMSprop(), metrics=['accuracy', Precision(), Recall(), MPDAmodel.f1_score])
        netModel.fit(X_train_all, Y_train_all, batch_size=BATCH_SIZE_NET, epochs=EPOCH_NET, validation_data=(X_val, Y_val))
        accr = netModel.evaluate(X_test, Y_test)
        netModel.save(write_h5_to, overwrite=True)

        print('{} Test set\n  Loss: {:0.3f}\n  Accuracy: {:0.3f}\n  Precision: {:0.3f}\n  Recall: {:0.3f}\n  F1Score: {:0.3f}\n'.format(cwe_name, accr[0], accr[1], accr[2], accr[3], accr[4]))


        filename = 'result/' + net + '_result.csv'
        new_data = {'CWE-name': cwe_name, 'Loss': accr[0], 'Accuracy': accr[1], 'Precision': accr[2], 'Recall': accr[3], 'F1Score': accr[4], 'length': length}

        if not os.path.isfile(filename):
            df = pd.DataFrame(columns=['CWE-name', 'Loss', 'Accuracy', 'Precision', 'Recall', 'F1Score', 'length', 'Placeholder',
                                    'Lossavg', 'Accuracyavg', 'Precisionavg', 'Recallavg', 'F1Scoreavg', 'Placeholder',
                                    'Lossmax', 'Accuracymax', 'Precisionmax', 'Recallmax', 'F1Scoremax', 'Placeholder',
                                    'Lossmin', 'Accuracymin', 'Precisionmin', 'Recallmin', 'F1Scoremin'])
            df.loc[0] = [new_data['CWE-name'], new_data['Loss'], new_data['Accuracy'], new_data['Precision'], new_data['Recall'], new_data['F1Score'], new_data['length'], '',
                        new_data['Loss'], new_data['Accuracy'], new_data['Precision'], new_data['Recall'], new_data['F1Score'], '',
                        new_data['Loss'], new_data['Accuracy'], new_data['Precision'], new_data['Recall'], new_data['F1Score'], '',
                        new_data['Loss'], new_data['Accuracy'], new_data['Precision'], new_data['Recall'], new_data['F1Score']]
            # df = pd.DataFrame(new_data, index=[0])
            df.to_csv(filename, index=False, float_format='%.3f')
        else:
            df = pd.read_csv(filename)
            grouped_df = df.groupby('CWE-name')
            if new_data['CWE-name'] in grouped_df.groups:
                group = grouped_df.get_group(new_data['CWE-name'])
                new_index = group.index[-1] + 1
                if new_index < len(df):
                    new_row = pd.DataFrame([new_data], columns=df.columns)
                    df = pd.concat([df.iloc[:new_index], new_row, df.iloc[new_index:]], ignore_index=True)

                group_mean = group.select_dtypes(include='number').mean().to_dict()
                group_max = group.select_dtypes(include='number').max().to_dict()
                group_min = group.select_dtypes(include='number').min().to_dict()
                for k, v in new_data.items():
                    if k in group_mean.keys():
                        group_mean[k] = (group_mean[k] * len(group) + v) / (len(group) + 1)
                    if k in group_max.keys():
                        group_max[k] = max(group_max[k], v)
                    if k in group_min.keys():
                        group_min[k] = min(group_min[k], v)
                new_data.update({k+'avg': v for k, v in group_mean.items() if k in new_data.keys()})
                new_data.update({k+'max': v for k, v in group_max.items() if k in new_data.keys()})
                new_data.update({k+'min': v for k, v in group_min.items() if k in new_data.keys()})
                df.loc[new_index] = [new_data['CWE-name'], new_data['Loss'], new_data['Accuracy'], new_data['Precision'], new_data['Recall'], new_data['F1Score'], new_data['length'], '',
                                    new_data['Lossavg'], new_data['Accuracyavg'], new_data['Precisionavg'], new_data['Recallavg'], new_data['F1Scoreavg'], '',
                                    new_data['Lossmax'], new_data['Accuracymax'], new_data['Precisionmax'], new_data['Recallmax'], new_data['F1Scoremax'], '',
                                    new_data['Lossmin'], new_data['Accuracymin'], new_data['Precisionmin'], new_data['Recallmin'], new_data['F1Scoremin']]
            else:
                new_index = len(df)
                df.loc[new_index] = [new_data['CWE-name'], new_data['Loss'], new_data['Accuracy'], new_data['Precision'], new_data['Recall'], new_data['F1Score'], new_data['length'], '',
                        new_data['Loss'], new_data['Accuracy'], new_data['Precision'], new_data['Recall'], new_data['F1Score'], '',
                        new_data['Loss'], new_data['Accuracy'], new_data['Precision'], new_data['Recall'], new_data['F1Score'], '',
                        new_data['Loss'], new_data['Accuracy'], new_data['Precision'], new_data['Recall'], new_data['F1Score']]
            df.to_csv(filename, index=False, float_format='%.3f')
        
