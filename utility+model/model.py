import tensorflow as tf
import keras as k
import numpy as np
import pickle
from keras.datasets import mnist
from keras.models import Sequential, Model
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers import Concatenate
from keras.optimizers import SGD, Adam, RMSprop, Adagrad
from keras.utils import np_utils
from keras.layers.convolutional import Conv2D,Conv3D
from keras.layers.convolutional import MaxPooling2D, MaxPooling3D

def feature_extractor(shape):
    model = Sequential()
    model.add(Conv2D(32, (3, 3), input_shape = shape, activation='relu',data_format="channels_first"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(15, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))
    model.add(Flatten())
    return model

def feature_extractor3D(shape):
    model = Sequential()
    model.add(Conv3D(64, (3, 3, 3), input_shape = shape, activation='relu',data_format="channels_first"))
    model.add(MaxPooling3D(pool_size=(2, 2)))
    model.add(Conv3D(32, (3, 3, 3), input_shape = shape, activation='relu'))
    model.add(MaxPooling3D(pool_size=(2, 2)))
    model.add(Conv3D(15, (3, 3, 3), activation='relu'))
    model.add(MaxPooling3D(pool_size=(2, 2)))
    model.add(Dropout(0.2))
    model.add(Flatten())
    return model

def label_classifier(model_1,model_2,model_3):
    mergeout = Concatenate()([model_1.output,model_2.output,model_3.output])
    mergeout = Dense(64, activation='relu')(mergeout)
    mergeout = Dense(32, activation='relu')(mergeout)
    mergeout = Dense(4, activation = 'softmax')(mergeout)
    return Model([model_1.input, model_2.input, model_3.input], mergeout)

def get_model(shape, dim = 2, option = 1):
    if(option == 1):
        if(dim == 2):
            fe_1 = feature_extractor(shape[0])
            fe_2 = feature_extractor(shape[1])
            fe_3 = feature_extractor(shape[2])
        else:
            fe_1 = feature_extractor3D(shape[0])
            fe_2 = feature_extractor3D(shape[1])
            fe_3 = feature_extractor3D(shape[2]) 
            return label_classifier(fe_1, fe_2, fe_3)
    else:
        fe = feature_extractor(shape)
        fe.add(Dense(64, activation='relu'))
        fe.add(Dense(32, activation='relu'))
        fe.add(Dense(4, activation = 'softmax'))
        return fe


def train(model, x_train, y_train):
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    history = model.fit(x = x_train, y = y_train, epochs = 15, verbose=1, validation_split = 0.2)
    return model, history

def save_history(history):
    with open('model/trainHistoryOld', 'wb') as handle: # saving the history of the model
        pickle.dump(history.history, handle)

def save_model(model):   
    model_json = model.to_json()
    with open('model/model_2D.json', 'w') as f:
        f.write(model_json)
    model.save_weights('model/model_2D.h5')


    




    
