import unittest
from EmotionDetection import emotion_detector
import json

class TestEmotionDetector(unittest.TestCase):
    def test_joy(self):
        response = json.loads(emotion_detector("I am glad this happened"))
        self.assertEqual(response["dominant_emotion"], "joy")

    def test_anger(self):
        response = json.loads(emotion_detector("I am really mad about this"))
        self.assertEqual(response["dominant_emotion"], "anger")

    def test_disgust(self):
        response = json.loads(emotion_detector("I feel disgusted just hearing about this"))
        self.assertEqual(response["dominant_emotion"], "disgust")

    def test_sadness(self):
        response = json.loads(emotion_detector("I am so sad about this"))
        self.assertEqual(response["dominant_emotion"], "sadness")

    def test_fear(self):
        response = json.loads(emotion_detector("I am really afraid that this will happen"))
        self.assertEqual(response["dominant_emotion"], "fear")

if __name__ == '__main__':
    unittest.main()
 