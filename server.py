"""
Flask application for emotion detection.
"""

from flask import Flask, render_template, request
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_function():
    """
    Analyzes the given text and returns the emotion detection result.

    Returns:
        str: A formatted string with detected emotions and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Error: No text provided for analysis."

    response = emotion_detector(text_to_analyze)

    if response['dominant_dictionary'] is None:
        response_text = "Invalid Input! Please try again."
    else:
        response_text = (
            f"For the given statement, the system response is 'anger': {response.get('anger', 0)}, "
            f"'disgust': {response.get('disgust', 0)}, 'fear': {response.get('fear', 0)}, "
            f"'joy': {response.get('joy', 0)}, 'sadness': {response.get('sadness', 0)}. "
            f"The dominant emotion is {response.get('dominant_dictionary', 'unknown')}."
        )

    return response_text

@app.route("/")
def render_index_page():
    """
    Renders the index page.

    Returns:
        str: HTML content of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
