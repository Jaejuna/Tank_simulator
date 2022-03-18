from keras.models import Input,Model
from keras.layers import Dense,Flatten,Reshape
from keras.layers.convolutional import Conv2D
from keras.callbacks import EarlyStopping
from keras.models import load_model
from board_conversion import *
import chess