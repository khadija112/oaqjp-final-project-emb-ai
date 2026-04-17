def emotion_detector(text_to_analyse):

    text = text_to_analyse.lower()

    if "happy" in text:
        emotions = {
            "anger": 0.01,
            "disgust": 0.01,
            "fear": 0.02,
            "joy": 0.95,
            "sadness": 0.01
        }

    elif "angry" in text:
        emotions = {
            "anger": 0.95,
            "disgust": 0.01,
            "fear": 0.02,
            "joy": 0.01,
            "sadness": 0.01
        }

    else:
        emotions = {
            "anger": 0.01,
            "disgust": 0.01,
            "fear": 0.01,
            "joy": 0.01,
            "sadness": 0.01
        }

    dominant = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],

        
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant
    }