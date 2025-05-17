from flask import Flask, render_template, request
from EmotionDetection import emotion_detector
import json
import requests

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Flask route to detect emotion from text input.
    Expects a 'textToAnalyze' query parameter.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    
    response_json = json.loads(emotion_detector(text_to_analyze))

    # Format the output string as per requirements
    output_string = (
        f"For the given statement, the system response is "
        f"'anger': {response_json['anger']}, "
        f"'disgust': {response_json['disgust']}, "
        f"'fear': {response_json['fear']}, "
        f"'joy': {response_json['joy']} and "
        f"'sadness': {response_json['sadness']}. "
        f"The dominant emotion is {response_json['dominant_emotion']}."
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