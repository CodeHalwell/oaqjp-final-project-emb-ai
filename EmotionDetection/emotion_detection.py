import requests
import json

def emotion_detector(text_to_analyze: str) -> dict:
    url: str = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header: dict[str] = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body: dict[str]= { "raw_document": { "text": text_to_analyze } }
    result = {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None
    }
    response = requests.post(url, headers=header, json=body)
    if response.status_code == 200:
        try:
            response_json = response.json()
            emotion_predictions = response_json['emotionPredictions'][0]['emotion']
            anger_score = emotion_predictions.get('anger')
            disgust_score = emotion_predictions.get('disgust')
            fear_score = emotion_predictions.get('fear')
            joy_score = emotion_predictions.get('joy')
            sadness_score = emotion_predictions.get('sadness')
            scores = {
                'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score
            }
            valid_scores = {k: v for k, v in scores.items() if isinstance(v, (int, float))}
            if not valid_scores: 
                    dominant_emotion = None
            else:
                dominant_emotion = max(valid_scores, key=valid_scores.get)
            result = {
                'anger': anger_score, 
                'disgust': disgust_score, 
                'fear': fear_score, 
                'joy': joy_score, 
                'sadness': sadness_score, 
                'dominant_emotion': dominant_emotion
            }
            return json.dumps(result, indent=4)
        except Exception:
            return json.dumps(result, indent=4)
    elif response.status_code == 400:
        return json.dumps(result, indent=4)
    else:
        return json.dumps(result, indent=4)