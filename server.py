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
    
    if not text_to_analyze:
        return "Error: No text provided for analysis. Please enter text and try again.", 400

    # Call the emotion_detector function (which returns a JSON string)
    response_json_str = emotion_detector(text_to_analyze)
    
    # Parse the JSON string to a Python dictionary
    try:
        response_dict = json.loads(response_json_str)
    except json.JSONDecodeError:
        return "Error: Invalid response format from emotion detector.", 500

    anger_score = response_dict.get('anger', 'N/A')
    disgust_score = response_dict.get('disgust', 'N/A')
    fear_score = response_dict.get('fear', 'N/A')
    joy_score = response_dict.get('joy', 'N/A')
    sadness_score = response_dict.get('sadness', 'N/A')
    dominant_emotion = response_dict.get('dominant_emotion', 'N/A')

    # Handle cases where dominant emotion might indicate an error or unknown state
    if "error" in dominant_emotion.lower() or "unknown" in dominant_emotion.lower() or dominant_emotion == 'N/A':
        return f"Could not process the statement: '{text_to_analyze}'. Reason: {dominant_emotion}", 200 # Or a 4xx/5xx error if preferred

    # Format the output string as per requirements
    output_string = (
        f"For the given statement, the system response is "
        f"'anger': {anger_score}, "
        f"'disgust': {disgust_score}, "
        f"'fear': {fear_score}, "
        f"'joy': {joy_score} and "
        f"'sadness': {sadness_score}. "
        f"The dominant emotion is {dominant_emotion}."
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