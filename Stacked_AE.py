#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@File    :   Stacked_AE.py
@Time    :   2021/11/03 20:04:14
@Author  :   Ray Zeng 
@Version :   1.0
@Contact :   11927025@zju.edu.cn
@License :   (C)Copyright
'''
# %%
# here put the import lib
import keras
from keras.layers import Input, Dropout
from keras.layers.core import Dense
from keras.models import Model, Sequential, load_model
from keras import regularizers
import tensorflow as tf
from numpy.random import seed
import matplotlib.pyplot as plt
from data_preprocess import Dataload_pure, min_max_normal, Dataload_smoothed, Dataload_pure

from keras import backend as K


# %%
class STACKEDAE(object):
    def __init__(self,
                 )