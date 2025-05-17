"""
Flask server for emotion detection.
Provides an API endpoint to analyze text for emotions and serves a simple web interface.
"""
import json
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Flask route to detect emotion from text input.
    Expects a 'textToAnalyze' query parameter.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response_dict = json.loads(emotion_detector(text_to_analyze))
    if (response_dict['dominant_emotion'] is None and
        all(value is None for value in response_dict.values())):
        return "<b>Invalid text! Please try again!</b>"
    output_string = (
        f"For the given statement, the system response is "
        f"'anger': {response_dict['anger']}, "
        f"'disgust': {response_dict['disgust']}, "
        f"'fear': {response_dict['fear']}, "
        f"'joy': {response_dict['joy']} and "
        f"'sadness': {response_dict['sadness']}. "
        f"The dominant emotion is <b>{response_dict['dominant_emotion']}</b>."
    )
    return output_string

@app.route("/")
def render_index_page():
    """
    Serves the main HTML page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Runs the Flask app on localhost with port 5000
    app.run(host="0.0.0.0", port=5000)
