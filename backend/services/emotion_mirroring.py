def detect_mirroring(user_msg, ai_msg):

    emotion_keywords = [
        "힘들", "외롭", "불안", "슬프", "지치", "무서","억울", "우울", "화나", "짜증", "속상", "아프", "괴롭", "지쳐","애정", "사랑", "행복", "즐거", "기쁘", "뿌듯", "감사", "자랑", "뭉클", "설레", "편안"
    ]

    user_emotions = [e for e in emotion_keywords if e in user_msg]
    ai_emotions = [e for e in emotion_keywords if e in ai_msg]

    # 공통 감정 있으면 미러링
    for e in user_emotions:
        if e in ai_emotions:
            return 1

    return 0