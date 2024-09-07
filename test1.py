import json
from EmotionDetection.emotion_detection import emotion_detector

result = emotion_detector("I am so happy I am doing this.")
ordered_result = {k: result[k] for k in result if k != 'dominant_emotion'}
ordered_result['dominant_emotion'] = result['dominant_emotion']

# Print the ordered result dictionary using json.dumps() for better formatting
print(json.dumps(ordered_result, indent=2))
