# Repository for final project

Comprehensive information
Project title: Emotion Detection
Description: This project provides an API endpoint to analyze text for emotions and serves a simple web interface. The emotions detected include anger, disgust, fear, joy, and sadness. The project uses IBM Watson's EmotionPredict API to analyze the text.
Installation instructions:
Clone the repository.
Install the required dependencies using pip install -r requirements.txt.
Usage instructions:
Run the Flask server using python server.py.
Open a web browser and navigate to http://localhost:5000.
Enter the text to be analyzed in the input field and click the "Run Sentiment Analysis" button.
The system will display the detected emotions and the dominant emotion.
License information: This project is licensed under the Apache License 2.0. See the 
LICENSE
 file for more details.
Additional information:
The main Flask server code is in 
server.py
.
The emotion detection logic is implemented in 
EmotionDetection/emotion_detection.py
.
The web interface is served using the template in 
templates/index.html
 and the JavaScript file 
static/mywebscript.js
.
Unit tests for the emotion detection logic are provided in 
test_emotion_detection.py
.
