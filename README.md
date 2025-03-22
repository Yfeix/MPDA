# MPDA
Replication code for MPDA. 
## Requirements
Python==3.9.21<br />
tensorflow-gpu==2.6.0<br />
keras==2.6.0<br />
numpy==1.19.5<br />
pytorch==2.5.1+cu121<br />
transformers==4.47.1<br />

## Files introduction
- **MPDA.py**
  - Program entry.
- **constants.py**
  - Hyper-parameter profile
- **oversample.py**
  - Use of multiple oversampling methods.
- **data_augmentation.py**
  - MPDA implementation.
- **embedding.py**
  - Data embedding, including Word2Vec, CodeBert, CodeT5+ and UniXcoder.
- **unixcoder.py**
  - UniXcoder pre-trained model run code from https://github.com/microsoft/CodeBERT.
- **model.py**
  - Models implementation and training, including lstm, gru, bilstm, bigru, bigru-att and transformer.
- **Transformer_Encoder.py**
  - Single-layer Tranformer encoder model implementation.
- **preprocessing.py**
  - Data preprocessing file, can this in the file switch mpda_compare.py and train_compare.py(only for specific experiment).
- **mpda_compare.py**
  - Model training setup file, the main file adjusted in the experiment. You can choose to train the model, as well as compare the effect on the raw data and MPDA.
- **train_compare.py**
  - For comparing the performace of augmented data and raw data in the same data size.

## Dataset
The dataset we are using is a collection of 29 vulnerabilities from the Juliet Test Suite dataset. We have provided in the ```./data``` directory. The vulnerability names and number of functions are shown in the following figure. You can find them in the https://github.com/find-sec-bugs/juliet-test-suite. The datasets are compressed and need to be unzipped before training:
```
cd data/cwe
unzip cwe.zip
rm cwe.zip
```



## Training models
First set up the relevant runtime settings in mpda_compare.py. For example:<br />
```
Model.train(cwe_name, 'bigru', 'mpda', i, X_train_all, Y_train_all, X_val, Y_val, X_test, Y_test, len(Y_train_all))
```
Then go to MPDA.py to set the number of loop experiments.<br />
Finally run the following command in a terminal.<br />
```
cd ../..                                 
python MPDA.py train "./data/cwe" 100    
```





