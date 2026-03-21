from backend.emotion_dictionary import emotion_dict


def extract_emotions(text):

    detected = set()

    for category, words in emotion_dict.items():

        for word in words:
            if word in text:
                detected.add(category)

    return detected

def detect_mirroring(user_msg, bot_msg):

    user_emotions = extract_emotions(user_msg)
    bot_emotions = extract_emotions(bot_msg)

    mirrored = user_emotions.intersection(bot_emotions)

    if mirrored:
        return 1
    else:
        return 0