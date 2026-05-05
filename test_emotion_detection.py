"""
Unit tests for the emotion_detector function in the EmotionDetection package.
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Unit test class for the emotion_detector function."""

    def test_joy_emotion(self):
        """Test that 'I am glad this happened' has dominant emotion joy."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_emotion(self):
        """Test that 'I am really mad about this' has dominant emotion anger."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_emotion(self):
        """Test that 'I feel disgusted just hearing about this' has dominant emotion disgust."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness_emotion(self):
        """Test that 'I am so sad about this' has dominant emotion sadness."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_emotion(self):
        """Test that 'I am really afraid that this will happen' has dominant emotion fear."""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
