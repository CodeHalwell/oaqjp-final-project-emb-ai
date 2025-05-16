import requests
import json


def emotion_detector(text_to_analyze: str) -> str:
    url: str = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header: dict[str] = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body: dict[str]= { "raw_document": { "text": text_to_analyze } }
    text = requests.post(url, headers=header, json=body).json()['emotionPredictions'][0]['emotion']

    anger_score, disgust_score, fear_score, joy_score, sadness_score = text['anger'], text['disgust'], text['fear'], text['joy'], text['sadness']

    scores = {
        'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score
    }

    valid_scores = {k: v for k, v in scores.items() if isinstance(v, (int, float))}
    dominant_emotion = max(valid_scores, key=valid_scores.get)
    result = {
        'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion
    }
    
    return json.dumps(result, indent=4)
    