import pandas as pd
import numpy as np
from keras import models
from keras.layers import Dense, Input, LeakyReLU, BatchNormalization
from keras.optimizers import Adam
from keras.models import load_model
from keras.utils import pad_sequences
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from constants import *
from oversample import Oversample

class Data_augmentation:

    @staticmethod
    def make_generator(input_dim, output_dim):
        model = models.Sequential()
        model.add(Dense(256, input_dim=input_dim, activation='relu'))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dense(512, activation='relu'))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dense(1024, activation='relu'))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Dense(output_dim, activation='tanh'))
        return model

    @staticmethod
    def make_discriminator(input_dim):
        model = models.Sequential()
        model.add(Dense(1024, input_dim=input_dim, activation='relu'))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dense(512, activation='relu'))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dense(256, activation='relu'))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dense(1, activation='sigmoid'))
        return model
    
    @staticmethod
    def make_gan(generator, discriminator):
        discriminator.trainable = False
        gan_input = generator.input
        gan_output = discriminator(generator.output)
        gan = models.Model(inputs=gan_input, outputs=gan_output)
        optimizer = Adam(learning_rate=0.0002, beta_1=0.5)
        gan.compile(loss='binary_crossentropy', optimizer=optimizer)
        return gan
    
    @staticmethod
    def train_gan(gan, generator, discriminator, X_train, BATCH_SIZE_GAN, epochs, vul_type, true):
        noise_input = np.random.randn(BATCH_SIZE_GAN, LATENT_DIM)
        real_labels = np.ones((BATCH_SIZE_GAN, 1))
        fake_labels = np.zeros((BATCH_SIZE_GAN, 1))

        for epoch in range(epochs):
            print("Epoch {} of {}".format(epoch+1, epochs))

            idx = np.random.randint(0, X_train.shape[0], BATCH_SIZE_GAN)
            real_data = X_train[idx]

            noise = np.random.randn(BATCH_SIZE_GAN, LATENT_DIM)
            fake_data = generator.predict(noise)

            d_loss_real = discriminator.train_on_batch(real_data, real_labels)
            d_loss_fake = discriminator.train_on_batch(fake_data, fake_labels)
            d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

            noise = np.random.randn(BATCH_SIZE_GAN, LATENT_DIM)
            g_loss = gan.train_on_batch(noise, real_labels)

            print("Epoch {}: Discriminator loss = {}, Generator loss = {}".format(epoch+1, d_loss, g_loss))
        
        if true == 0:
            generator.save('GAN/' + vul_type + '_true_generator_model.h5')
            discriminator.save('GAN/' + vul_type + '_true_discriminator_model.h5')
        else:
            generator.save('GAN/' + vul_type + '_false_generator_model.h5')
            discriminator.save('GAN/' + vul_type + '_false_discriminator_model.h5')

    @staticmethod
    def add_gaussian_noise(data, mean=0, std=np.sqrt(0.01)):
        noise = np.random.normal(mean, std, data.shape)
        return data + noise

    @staticmethod
    def data_augmentation(X_train, Y_train, vul_type, net_type):

        X_train_2d = X_train.reshape(X_train.shape[0], -1)

        X_train_2d_resampled, Y_resampled = Oversample.oversample(X_train_2d, Y_train, vul_type)

        X_resampled = X_train_2d_resampled.reshape(X_train_2d_resampled.shape[0], MAX_LEN, 150)

        X_true = X_train_2d_resampled[Y_resampled[:, 0] == 0, :]
        X_false = X_train_2d_resampled[Y_resampled[:, 0] == 1, :]

        # true sample

        output_dim = X_true.shape[1]

        generator_true = Data_augmentation.make_generator(input_dim, np.prod(output_dim))
        discriminator_true = Data_augmentation.make_discriminator(np.prod(output_dim))

        discriminator_true.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.0002, beta_1=0.5), metrics=['accuracy'])

        gan_true = Data_augmentation.make_gan(generator_true, discriminator_true)

        gan_true.summary()

        Data_augmentation.train_gan(gan_true, generator_true, discriminator_true, X_true, BATCH_SIZE_GAN, BATCH_SIZE_NET, vul_type, 0)

        true_generator = load_model('GAN/' + vul_type + '_true_generator_model.h5', compile=False)

        num_samples_true = int(X_true.shape[0] / 4)
        print('num_samples : {}', num_samples_true)

        z = np.random.normal(size=(num_samples_true, LATENT_DIM))

        X_true_2d = true_generator.predict(z)

        # false sample

        output_dim = X_false.shape[1]

        generator_false = Data_augmentation.make_generator(input_dim, np.prod(output_dim))
        discriminator_false = Data_augmentation.make_discriminator(np.prod(output_dim))

        discriminator_false.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.0002, beta_1=0.5), metrics=['accuracy'])

        gan_false = Data_augmentation.make_gan(generator_false, discriminator_false)

        gan_false.summary()

        Data_augmentation.train_gan(gan_false, generator_false, discriminator_false, X_false, BATCH_SIZE_GAN, BATCH_SIZE_NET, vul_type, 1)

        false_generator = load_model('GAN/' + vul_type + '_false_generator_model.h5', compile=False)

        num_samples_false = int(X_false.shape[0] / 4)
        print('num_samples : {}', num_samples_false)

        z = np.random.normal(size=(num_samples_false, LATENT_DIM))

        X_false_2d = false_generator.predict(z)

        ##################################################################################################################################
        # GAN
        X_gan_true = X_true_2d.reshape(X_true_2d.shape[0], MAX_LEN, 150)
        Y_gan_true = np.zeros((num_samples_true, 1), dtype=int)

        X_gan_false = X_false_2d.reshape(X_false_2d.shape[0], MAX_LEN, 150)
        Y_gan_false = np.ones((num_samples_false, 1), dtype=int)


        # GAN_Fsample
        noisy_data_true = Data_augmentation.add_gaussian_noise(X_true_2d, mean=0, std=np.sqrt(0.01))
        noisy_data_false = Data_augmentation.add_gaussian_noise(X_false_2d, mean=0, std=np.sqrt(0.01))

        X_gan_true_Fsample = noisy_data_true.reshape(noisy_data_true.shape[0], MAX_LEN, 150)
        Y_gan_true_Fsample = np.zeros((num_samples_true, 1), dtype=int)

        X_gan_false_Fsample = noisy_data_false.reshape(noisy_data_false.shape[0], MAX_LEN, 150)
        Y_gan_false_Fsample = np.ones((num_samples_false, 1), dtype=int)

        # Fsample
        X_Fsampling_2d = Data_augmentation.add_gaussian_noise(X_train_2d, mean=0, std=np.sqrt(0.01))
        X_Fsampling = X_Fsampling_2d.reshape(X_Fsampling_2d.shape[0], MAX_LEN, 150)

        # Oversample_Fsample
        X_resampled_Fsample_2d = Data_augmentation.add_gaussian_noise(X_train_2d_resampled, mean=0, std=np.sqrt(0.01))
        X_resampled_Fsample = X_resampled_Fsample_2d.reshape(X_resampled_Fsample_2d.shape[0], MAX_LEN, 150)


        ##################################################################################################################################

        # 1 Oversample + GAN_Fsample
        if vul_type == "CWE197" or vul_type == "CWE789" or vul_type == "CWE81":


            X_all_false_Fsample = np.concatenate((X_resampled, X_gan_false_Fsample), axis=0)
            Y_all_false_Fsample = np.concatenate((Y_resampled, Y_gan_false_Fsample), axis=0)

            X_all_Fsample = np.concatenate((X_all_false_Fsample, X_gan_true_Fsample), axis=0)
            Y_all_Fsample = np.concatenate((Y_all_false_Fsample, Y_gan_true_Fsample), axis=0)

            X_all_Fsample, Y_all_Fsample = shuffle(X_all_Fsample, Y_all_Fsample)

            return X_all_Fsample, Y_all_Fsample


        ##################################################################################################################################

        # 2 Oversample_Fsample + GAN

        elif vul_type == "CWE129" or vul_type == "CWE15" or vul_type == "CWE190" or vul_type == "CWE23" or vul_type == "CWE259"\
              or vul_type == "CWE319" or vul_type == "CWE369" or vul_type == "CWE563" or vul_type == "CWE606"\
                or vul_type == "CWE690" or vul_type == "CWE78":

            X_resample_Fsample_gan_false = np.concatenate((X_resampled_Fsample, X_gan_false), axis=0)
            Y_resample_Fsample_gan_false = np.concatenate((Y_resampled, Y_gan_false), axis=0)

            X_resample_Fsample_gan = np.concatenate((X_resample_Fsample_gan_false, X_gan_true), axis=0)
            Y_resample_Fsample_gan = np.concatenate((Y_resample_Fsample_gan_false, Y_gan_true), axis=0)

            X_resample_Fsample_gan_all = np.concatenate((X_resample_Fsample_gan, X_resampled), axis=0)
            Y_resample_Fsample_gan_all = np.concatenate((Y_resample_Fsample_gan, Y_resampled), axis=0)

            X_resample_Fsample_gan_all, Y_resample_Fsample_gan_all = shuffle(X_resample_Fsample_gan_all, Y_resample_Fsample_gan_all)

            return X_resample_Fsample_gan_all, Y_resample_Fsample_gan_all

        ###################################################################################################################################

        # 3 Oversample_Fsample + GAN_Fsample

        elif vul_type == "CWE113" or vul_type == "CWE134" or vul_type == "CWE191" or vul_type == "CWE506" or vul_type == "CWE601"\
              or vul_type == "CWE83" or vul_type == "CWE89" or vul_type == "CWE90":

            X_resample_Fsample_gan_Fsample_false = np.concatenate((X_resampled_Fsample, X_gan_false_Fsample), axis=0)
            Y_resample_Fsample_gan_Fsample_false = np.concatenate((Y_resampled, Y_gan_false_Fsample), axis=0)

            X_resample_Fsample_gan_Fsample = np.concatenate((X_resample_Fsample_gan_Fsample_false, X_gan_true_Fsample), axis=0)
            Y_resample_Fsample_gan_Fsample = np.concatenate((Y_resample_Fsample_gan_Fsample_false, Y_gan_true_Fsample), axis=0)

            X_resample_Fsample_gan_Fsample_all = np.concatenate((X_resample_Fsample_gan_Fsample, X_resampled), axis=0)
            Y_resample_Fsample_gan_Fsample_all = np.concatenate((Y_resample_Fsample_gan_Fsample, Y_resampled), axis=0)

            X_resample_Fsample_gan_Fsample_all, Y_resample_Fsample_gan_Fsample_all = shuffle(X_resample_Fsample_gan_Fsample_all, Y_resample_Fsample_gan_Fsample_all)

            return X_resample_Fsample_gan_Fsample_all, Y_resample_Fsample_gan_Fsample_all
        ###################################################################################################################################

        # 4 Fsample + Oversample + GAN

        elif vul_type == "CWE36" or vul_type == "CWE398" or vul_type == "CWE400" or vul_type == "CWE470" or vul_type == "CWE476"\
              or vul_type == "CWE643" or vul_type == "CWE80":

            X_all_false = np.concatenate((X_resampled, X_gan_false), axis=0)
            Y_all_false = np.concatenate((Y_resampled, Y_gan_false), axis=0)

            X_all = np.concatenate((X_all_false, X_gan_true), axis=0)
            Y_all = np.concatenate((Y_all_false, Y_gan_true), axis=0)

            X_all, Y_all = shuffle(X_all, Y_all)
            X_Fsample_Oversample_gan = np.concatenate((X_all, X_Fsampling), axis=0)
            Y_Fsample_Oversample_gan = np.concatenate((Y_all, Y_train), axis=0)

            X_Fsample_Oversample_gan, Y_Fsample_Oversample_gan = shuffle(X_Fsample_Oversample_gan, Y_Fsample_Oversample_gan)

            return X_Fsample_Oversample_gan, Y_Fsample_Oversample_gan
        

        ###################################################################################################################################
        # unknow
        else:
            if net_type == "basic":
                # 2 Oversample_Fsample + GAN
                X_resample_Fsample_gan_false = np.concatenate((X_resampled_Fsample, X_gan_false), axis=0)
                Y_resample_Fsample_gan_false = np.concatenate((Y_resampled, Y_gan_false), axis=0)

                X_resample_Fsample_gan = np.concatenate((X_resample_Fsample_gan_false, X_gan_true), axis=0)
                Y_resample_Fsample_gan = np.concatenate((Y_resample_Fsample_gan_false, Y_gan_true), axis=0)

                X_resample_Fsample_gan_all = np.concatenate((X_resample_Fsample_gan, X_resampled), axis=0)
                Y_resample_Fsample_gan_all = np.concatenate((Y_resample_Fsample_gan, Y_resampled), axis=0)

                X_resample_Fsample_gan_all, Y_resample_Fsample_gan_all = shuffle(X_resample_Fsample_gan_all, Y_resample_Fsample_gan_all)

                return X_resample_Fsample_gan_all, Y_resample_Fsample_gan_all
            
            elif net_type == "advanced":
            
                # 3 Oversample_Fsample + GAN_Fsample
                X_resample_Fsample_gan_Fsample_false = np.concatenate((X_resampled_Fsample, X_gan_false_Fsample), axis=0)
                Y_resample_Fsample_gan_Fsample_false = np.concatenate((Y_resampled, Y_gan_false_Fsample), axis=0)

                X_resample_Fsample_gan_Fsample = np.concatenate((X_resample_Fsample_gan_Fsample_false, X_gan_true_Fsample), axis=0)
                Y_resample_Fsample_gan_Fsample = np.concatenate((Y_resample_Fsample_gan_Fsample_false, Y_gan_true_Fsample), axis=0)

                X_resample_Fsample_gan_Fsample_all = np.concatenate((X_resample_Fsample_gan_Fsample, X_resampled), axis=0)
                Y_resample_Fsample_gan_Fsample_all = np.concatenate((Y_resample_Fsample_gan_Fsample, Y_resampled), axis=0)

                X_resample_Fsample_gan_Fsample_all, Y_resample_Fsample_gan_Fsample_all = shuffle(X_resample_Fsample_gan_Fsample_all, Y_resample_Fsample_gan_Fsample_all)

                return X_resample_Fsample_gan_Fsample_all, Y_resample_Fsample_gan_Fsample_all
