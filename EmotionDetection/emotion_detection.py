import requests


def emotion_detector(text_to_analyse):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Create the payload with the text to be analyzed
    myobj = {"raw_document": {"text": text_to_analyse}}
    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    result = None
    try:
        response = requests.post(url, json=myobj, headers=header, timeout=10)
        if response.status_code == 200:
            # Parse the response from the API
            formatted_response = response.json()
            result = formatted_response['emotionPredictions'][0]['emotion']
            result['dominant_emotion'] = max(result, key=result.get)
        elif response.status_code == 400:
            result = {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        else:
            # Handle non-200 responses
            print(f"Error: Received status code {response.status_code}. Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return result
