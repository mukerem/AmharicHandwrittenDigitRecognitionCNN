
from tensorflow import keras

def model_construct():
    model = keras.models.load_model('digit/25-epoch-val-acc-93-64-lr-1e-3-batch-128.h5')
    return model