from tensorflow.keras import Model
from tensorflow.keras.applications.inception_v3 import InceptionV3
import numpy as np
import cv2


def encoder_model(model):
    new_input = model.input
    new_output = model.layers[-2].output
    img_encoder = Model(new_input, new_output)
    return img_encoder


def encode_images(image):
    img_model = InceptionV3(weights='imagenet') #Replace with Resnet if Resnet50 works better
    model = encoder_model(img_model)
    image = np.expand_dims(np.asarray(cv2.resize(image, (299, 299))) / 255.0, axis=0)
    enc_train = model.predict(image)
    print(enc_train.shape)
    return enc_train