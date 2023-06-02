from flask import Flask, render_template, request
import news_preprocessing

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", alert_message="")

@app.route("/prediction", methods=['POST'])
def prediction():
    news = request.form['news']
    preprocessed_news = news_preprocessing.news_preprocess(news)
    prediction = news_preprocessing.predict(preprocessed_news)
    return render_template("prediction.html", news=news, real_fake=prediction[0], confidence=prediction[1])
