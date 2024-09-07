from EmotionDetection.emotion_detection import emotion_detector
import unittest


class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        self.assertEqual(self.get_dominant_emotion("I am glad this happened"),
                         "joy")
        self.assertEqual(self.get_dominant_emotion("I am really mad about this"),
                         "anger")
        self.assertEqual(self.get_dominant_emotion("I feel disgusted just hearing about this"),
                         "disgust")
        self.assertEqual(self.get_dominant_emotion("I am so sad about this"),
                         "sadness")
        self.assertEqual(self.get_dominant_emotion("I am really afraid that this will happen"),
                         "fear")

    def get_dominant_emotion(self, text):
        return emotion_detector(text)['dominant_emotion']


if __name__ == "__main__":
    unittest.main()
