import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences

def news_preprocess(news):
    with open('fake-news-model/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    sequence = tokenizer.texts_to_sequences([news])
    # print(sequence)
    padd = pad_sequences(sequence, maxlen=500, padding='post', truncating='post')
    # print(len(padd[0]))
    return padd

def predict(news):
    loaded_model = tf.keras.saving.load_model(
    'fake-news-model/model.keras', custom_objects=None, compile=True, safe_mode=True)
    value = loaded_model.predict(news)[0][0]
    # formatted_value = float("{:6.2f}".format(value * 100))

    if(value > 0.5):
        return ["Fake", value*100]
    else:
        return ["Real", value * 100]