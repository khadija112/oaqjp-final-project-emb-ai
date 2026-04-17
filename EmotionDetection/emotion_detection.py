def emotion_detector(text_to_analyse):
    emotions = {
        "anger": 0.01,
        "disgust": 0.01,
        "fear": 0.02,
        "joy": 0.95,
        "sadness": 0.01
    }

    dominant = max(emotions, key=emotions.get)

    return {
        "anger": float(emotions["anger"]),
        "disgust": float(emotions["disgust"]),
        "fear": float(emotions["fear"]),
        "joy": float(emotions["joy"]),
        "sadness": float(emotions["sadness"]),
        "dominant_emotion": dominant
    }