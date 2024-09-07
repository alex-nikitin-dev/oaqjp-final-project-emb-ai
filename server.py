"""
Emotion Detector Flask Application
This module implements a Flask web application for detecting emotions in a given text input.
The application uses the `emotion_detector()` function from the `EmotionDetection.emotion_detection` 
module to analyze the text provided by the user via an HTML interface.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


# Initiate the flask app
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from the HTML interface and
        runs emotion detector over it using emotion_detector()
        function. The output returned shows the required set of emotions, 
        including anger, disgust, fear, joy and sadness, along with their scores,
        aditionally shows 'dominant_emotion'
    '''
    text = request.args.get("textToAnalyze")
    if text is None:
        return {"message": "Query parameter textToAnalyze is missing"}

    res = emotion_detector(text)

    if res is None:
        return "AI Analysis Server error occures"
    if res['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    emotions = ', '.join(
    f"'{key}': {value}" 
    for key, value in res.items()
    if key != 'dominant_emotion'
    )
    return (f"For the given statement, the system response is "
            f"{emotions}."
            f"<br/> The dominant emotion is <b>{res['dominant_emotion']}.</b>")


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")


if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000,debug=True)
