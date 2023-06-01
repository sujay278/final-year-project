from flask import Flask, render_template, request
import tensorflow as tf
# import newspreprocessing
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", alert_message="")

@app.route("/prediction", methods=['POST'])
def prediction():
    news = request.form['news']
    # tf.keras.load_model()
    # preprocessed_news = preprocess(news)
    # prediction = newspreprocessing.predict(preprocessed_news)
    # prediction = "Nishant R Shinde"
    return render_template("prediction.html", news=news, predicted_value=prediction)

def preprocess(news):
    return 