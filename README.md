# Emotion Detection 😡🤢😨😄😢
This project provides an API endpoint to analyze text for emotions and serves a simple web interface. The emotions detected include anger, disgust, fear, joy, and sadness. The project utilizes IBM Watson's Natural Language Understanding API (specifically, the emotion analysis feature) to analyze the text.

## Features ✨
Analyzes text to detect five primary emotions: anger, disgust, fear, joy, and sadness.
Identifies the dominant emotion from the analyzed text.
Provides a simple and intuitive web interface for easy interaction.
Utilizes IBM Watson's powerful AI for accurate emotion analysis.

## Technology Stack 💻
Backend: Python, Flask
Emotion Analysis: IBM Watson Natural Language Understanding API
Frontend: HTML, JavaScript
Testing: Python's unittest module

## Installation Instructions ⚙️
Clone the repository:
```Bash

git clone <your-repository-url>
cd <repository-folder-name>
```
Create and activate a virtual environment (recommended):

```Bash

python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

## Usage Instructions ▶️
Run the Flask server:
```Bash

python server.py
```

Open a web browser and navigate to: http://localhost:5000
Enter the text to be analyzed in the input field.
Click the "Run Sentiment Analysis" button.
The system will display the detected emotions (scores for anger, disgust, fear, joy, sadness) and the dominant emotion.

## API Endpoint ↔️
The core emotion analysis logic is exposed via an API endpoint handled by the Flask application.

Endpoint: /emotionDetector (or similar, check server.py)

Method: POST 

Query Parameter: textToAnalyze (or similar, check server.py)

Response: JSON object containing the scores for each emotion and the dominant emotion.

Example Response:

```JSON

{
  "anger": 0.040965,
  "disgust": 0.014083,
  "fear": 0.004912,
  "joy": 0.917685,
  "sadness": 0.040965,
  "dominant_emotion": "joy"
}
```

## Key Files Overview 📜

server.py: This is the main entry point for the application. It sets up the Flask web server, defines routes (like the homepage and the API endpoint for emotion analysis), and handles requests and responses.
EmotionDetection/emotion_detection.py: This module contains the core logic for interacting with the IBM Watson API. It takes text as input, sends it to the Watson service, and processes the response to extract emotion scores.
templates/index.html: This HTML file defines the structure and content of the web interface that users interact with. It includes the input field for text and the area where results are displayed.
static/mywebscript.js: This JavaScript file handles the client-side interactivity of the web page. It likely captures the text input, makes an AJAX request to the Flask backend API, and then updates the HTML to display the emotion analysis results.
test_emotion_detection.py: This file contains unit tests specifically for the emotion_detection.py module. These tests ensure that the emotion detection functions work correctly, for example, by testing with known inputs and expected outputs (e.g., handling empty input, or specific phrases that should elicit certain emotions).
.gitignore: Specifies intentionally untracked files that Git should ignore, such as virtual environment folders, sensitive credential files (like .env), and compiled Python files (__pycache__).
LICENSE: Contains the terms and conditions under which the project's source code is made available. In this case, it's the Apache License 2.0.

## Testing 🧪
Unit tests for the emotion detection logic are provided in test_emotion_detection.py. These tests help ensure the reliability and correctness of the core analysis functionality.

To run the tests (assuming they are written using a framework like unittest or pytest):

```Bash

python -m unittest test_emotion_detection.py
```
or if using pytest:
```
Bash

pytest
```

## License Information ⚖️
This project is licensed under the Apache License 2.0. See the LICENSE file for more details.

## Potential Future Enhancements 🚀
Support for analyzing text from URLs or uploaded documents.
Visualization of emotion scores (e.g., bar charts).
Batch processing for analyzing multiple texts at once.
User authentication and history of analyses.
More sophisticated error handling and user feedback.
Containerization with Docker for easier deployment.

## Author(s) ✍️
CodeHalwell 

