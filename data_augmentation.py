import pandas as pd
import numpy as np
from keras import models
from keras.layers import Dense, Input, LeakyReLU, BatchNormalization
from tensorflow.keras.optimizers import Adam
from keras.models import load_model
# from keras.utils import pad_sequences
# from keras.utils.data_utils import pad_sequences
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from constants import *
from oversample import Oversample
from tqdm import tqdm

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
    def train_gan(gan, generator, discriminator, X_train, batch_size, epochs, vul_type, true, net):

        noise_input = np.random.randn(batch_size, LATENT_DIM)

        real_labels = np.ones((batch_size, 1))

        fake_labels = np.zeros((batch_size, 1))

        loop = tqdm(range(epochs), ncols=150)
        for epoch in loop:

            idx = np.random.randint(0, X_train.shape[0], batch_size)
            real_data = X_train[idx]

            noise = np.random.randn(batch_size, LATENT_DIM)
            fake_data = generator.predict(noise)

            d_loss_real = discriminator.train_on_batch(real_data, real_labels)
            d_loss_fake = discriminator.train_on_batch(fake_data, fake_labels)
            d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)


            noise = np.random.randn(batch_size, LATENT_DIM)

            g_loss = gan.train_on_batch(noise, real_labels)

            loop.set_description(f'Training GAN Epoch [{epoch+1}/{epochs}]')
            loop.set_postfix({'Discriminator loss':[f'{x:.5f}' for x in d_loss], 'Generator loss': f'{g_loss:.4f}'})

        return generator
        
        # if true == 0:
        #     generator.save('GAN/' + vul_type + net + '_true_generator_model.h5')
        #     discriminator.save('GAN/' + vul_type + net + '_true_discriminator_model.h5')
        # else:
        #     generator.save('GAN/' + vul_type + net + '_false_generator_model.h5')
        #     discriminator.save('GAN/' + vul_type + net + '_false_discriminator_model.h5')

    @staticmethod
    def add_gaussian_noise(data, mean=0, std=np.sqrt(0.01)):
        noise = np.random.normal(mean, std, data.shape)
        return data + noise

    @staticmethod
    def data_augmentation(X_train, Y_train, vul_type, net_type, net):

        X_train_2d = X_train.reshape(X_train.shape[0], -1)


        X_train_2d_resampled, Y_resampled = Oversample.oversample(X_train_2d, Y_train, vul_type)


        X_resampled = X_train_2d_resampled.reshape(X_train_2d_resampled.shape[0], MAX_LEN, INPUT_SIZE)


        X_true = X_train_2d_resampled[Y_resampled[:, 0] == 0, :]
        X_false = X_train_2d_resampled[Y_resampled[:, 0] == 1, :]


        output_dim = X_true.shape[1]

        generator_true = Data_augmentation.make_generator(input_dim, np.prod(output_dim))
        discriminator_true = Data_augmentation.make_discriminator(np.prod(output_dim))

        discriminator_true.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.0002, beta_1=0.5), metrics=['accuracy'])

        gan_true = Data_augmentation.make_gan(generator_true, discriminator_true)

        gan_true.summary()

        # Data_augmentation.train_gan(gan_true, generator_true, discriminator_true, X_true, BATCH_SIZE_GAN, EPOCH_GAN, vul_type, 0, net)
        # true_generator = load_model('GAN/' + vul_type + net + '_true_generator_model.h5', compile=False)

        # unsave the model.
        true_generator = Data_augmentation.train_gan(gan_true, generator_true, discriminator_true, X_true, BATCH_SIZE_GAN, EPOCH_GAN, vul_type, 0, net)


        num_samples_true = int(X_true.shape[0] / 4)
        print('num_samples : {}'.format(num_samples_true))


        z = np.random.normal(size=(num_samples_true, LATENT_DIM))


        X_true_2d = true_generator.predict(z)



        output_dim = X_false.shape[1]

        generator_false = Data_augmentation.make_generator(input_dim, np.prod(output_dim))
        discriminator_false = Data_augmentation.make_discriminator(np.prod(output_dim))

        discriminator_false.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.0002, beta_1=0.5), metrics=['accuracy'])

        gan_false = Data_augmentation.make_gan(generator_false, discriminator_false)

        gan_false.summary()

        # Data_augmentation.train_gan(gan_false, generator_false, discriminator_false, X_false, BATCH_SIZE_GAN, EPOCH_GAN, vul_type, 1, net)
        # false_generator = load_model('GAN/' + vul_type + net + '_false_generator_model.h5', compile=False)

        # unsave the model.
        false_generator = Data_augmentation.train_gan(gan_false, generator_false, discriminator_false, X_false, BATCH_SIZE_GAN, EPOCH_GAN, vul_type, 1, net)


        num_samples_false = int(X_false.shape[0] / 4)
        print('num_samples : {}'.format(num_samples_false))

        z = np.random.normal(size=(num_samples_false, LATENT_DIM))

        X_false_2d = false_generator.predict(z)

        ##################################################################################################################################

        # GAN
        X_gan_true = X_true_2d.reshape(X_true_2d.shape[0], MAX_LEN, INPUT_SIZE)
        Y_gan_true = np.zeros((num_samples_true, 1), dtype=int)

        X_gan_false = X_false_2d.reshape(X_false_2d.shape[0], MAX_LEN, INPUT_SIZE)
        Y_gan_false = np.ones((num_samples_false, 1), dtype=int)


        # GAN_Fsample
        noisy_data_true = Data_augmentation.add_gaussian_noise(X_true_2d, mean=0, std=np.sqrt(0.01))
        noisy_data_false = Data_augmentation.add_gaussian_noise(X_false_2d, mean=0, std=np.sqrt(0.01))

        X_gan_true_Fsample = noisy_data_true.reshape(noisy_data_true.shape[0], MAX_LEN, INPUT_SIZE)
        Y_gan_true_Fsample = np.zeros((num_samples_true, 1), dtype=int)

        X_gan_false_Fsample = noisy_data_false.reshape(noisy_data_false.shape[0], MAX_LEN, INPUT_SIZE)
        Y_gan_false_Fsample = np.ones((num_samples_false, 1), dtype=int)

        # Fsample
        X_Fsampling_2d = Data_augmentation.add_gaussian_noise(X_train_2d, mean=0, std=np.sqrt(0.01))
        X_Fsampling = X_Fsampling_2d.reshape(X_Fsampling_2d.shape[0], MAX_LEN, INPUT_SIZE)

        # Oversample_Fsample
        X_resampled_Fsample_2d = Data_augmentation.add_gaussian_noise(X_train_2d_resampled, mean=0, std=np.sqrt(0.01))
        X_resampled_Fsample = X_resampled_Fsample_2d.reshape(X_resampled_Fsample_2d.shape[0], MAX_LEN, INPUT_SIZE)


        ##################################################################################################################################

        # strategy 1 Oversample + GAN_Fsample
        if vul_type == "CWE197" or vul_type == "CWE789" or vul_type == "CWE81":


            X_all_false_Fsample = np.concatenate((X_resampled, X_gan_false_Fsample), axis=0)
            Y_all_false_Fsample = np.concatenate((Y_resampled, Y_gan_false_Fsample), axis=0)

            X_all_Fsample = np.concatenate((X_all_false_Fsample, X_gan_true_Fsample), axis=0)
            Y_all_Fsample = np.concatenate((Y_all_false_Fsample, Y_gan_true_Fsample), axis=0)

            X_all_Fsample, Y_all_Fsample = shuffle(X_all_Fsample, Y_all_Fsample)

            return X_all_Fsample, Y_all_Fsample


        ##################################################################################################################################

        # strategy2 Oversample_Fsample + GAN + Oversample

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

        # strategy3 Oversample_Fsample + GAN_Fsample + Oversample

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

        # strategy4 Fsample + Oversample + GAN

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
        # unknown cwe types
        else:
            if net_type == "basic":
                X_resample_Fsample_gan_false = np.concatenate((X_resampled_Fsample, X_gan_false), axis=0)
                Y_resample_Fsample_gan_false = np.concatenate((Y_resampled, Y_gan_false), axis=0)

                X_resample_Fsample_gan = np.concatenate((X_resample_Fsample_gan_false, X_gan_true), axis=0)
                Y_resample_Fsample_gan = np.concatenate((Y_resample_Fsample_gan_false, Y_gan_true), axis=0)

                X_resample_Fsample_gan_all = np.concatenate((X_resample_Fsample_gan, X_resampled), axis=0)
                Y_resample_Fsample_gan_all = np.concatenate((Y_resample_Fsample_gan, Y_resampled), axis=0)

                X_resample_Fsample_gan_all, Y_resample_Fsample_gan_all = shuffle(X_resample_Fsample_gan_all, Y_resample_Fsample_gan_all)

                return X_resample_Fsample_gan_all, Y_resample_Fsample_gan_all
            
            elif net_type == "advanced":
            
                X_resample_Fsample_gan_Fsample_false = np.concatenate((X_resampled_Fsample, X_gan_false_Fsample), axis=0)
                Y_resample_Fsample_gan_Fsample_false = np.concatenate((Y_resampled, Y_gan_false_Fsample), axis=0)

                X_resample_Fsample_gan_Fsample = np.concatenate((X_resample_Fsample_gan_Fsample_false, X_gan_true_Fsample), axis=0)
                Y_resample_Fsample_gan_Fsample = np.concatenate((Y_resample_Fsample_gan_Fsample_false, Y_gan_true_Fsample), axis=0)

                X_resample_Fsample_gan_Fsample_all = np.concatenate((X_resample_Fsample_gan_Fsample, X_resampled), axis=0)
                Y_resample_Fsample_gan_Fsample_all = np.concatenate((Y_resample_Fsample_gan_Fsample, Y_resampled), axis=0)

                X_resample_Fsample_gan_Fsample_all, Y_resample_Fsample_gan_Fsample_all = shuffle(X_resample_Fsample_gan_Fsample_all, Y_resample_Fsample_gan_Fsample_all)

                return X_resample_Fsample_gan_Fsample_all, Y_resample_Fsample_gan_Fsample_all
