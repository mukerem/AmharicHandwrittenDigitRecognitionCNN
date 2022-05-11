
from tensorflow import keras

def model_construct():
    model = keras.models.load_model('20-epoch-val-acc-94-84-lr-1e-3-batch-32-nadam.h5')
    return model