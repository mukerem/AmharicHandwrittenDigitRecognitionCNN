
from tensorflow import keras

def model_construct():
    model = keras.models.load_model('30-epoch-acc-96-21-lr-1e-3-batch-32-nadam.h5')
    return model
