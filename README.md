# Emotion Detector: AI-Based Flask Web Application

This project is a web-based application built with Flask that analyzes emotions in a given text input using an AI-powered emotion detection model provided by IBM Watson. The application provides insights into the emotions present in the text, including anger, disgust, fear, joy, and sadness, and identifies the dominant emotion.

## Features

- **Emotion Analysis**: Detects emotions such as anger, disgust, fear, joy, and sadness from a provided text input.
- **Dominant Emotion Identification**: Highlights the dominant emotion among the detected emotions.
- **User-Friendly Interface**: A simple web interface where users can input text and view the emotional analysis.
- **Error Handling**: Provides meaningful error messages for missing or invalid input.
- **Integration with IBM Watson AI**: Utilizes IBM Watson's NLP Service for emotion analysis.

## Technologies Used

- **Python**: Core programming language used for backend development.
- **Flask**: Micro web framework for handling HTTP requests and serving web pages.
- **HTML**: Used for the front-end interface (`index.html`).
- **Requests**: Python library for making HTTP requests to the IBM Watson API.
- **IBM Watson NLP API**: IBM's Natural Language Processing service is used to analyze emotions in text.
- **Unittest**: Python's built-in testing framework for testing the emotion detection functionality.

## IBM Watson Integration

This project uses IBM Watson's NLP API to perform emotion detection. The `emotion_detector()` function sends a POST request to the IBM Watson API endpoint with the text to be analyzed and processes the response to extract the emotion scores.

- **API Endpoint**: `https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict`
- **Required Header**: `grpc-metadata-mm-model-id` with the value `emotion_aggregated-workflow_lang_en_stock`.
- **Request Format**: A JSON payload containing the text to be analyzed.


![image](https://github.com/user-attachments/assets/d09b857b-928d-41e3-95b5-e973a6c8b4ff)
