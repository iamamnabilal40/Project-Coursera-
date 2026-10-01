import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"Grpc-Metadata-mm-model-id": "annotator_watson_nlp.emotion_staff.emotion_distilbert-base"}
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)
    return formatted_response['emotionPredictions'][0]['emotion']
  
