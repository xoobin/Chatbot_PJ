def generate_prompt(user_message, risk_level):

    if risk_level == "low":

        system_prompt = """
당신은 친절한 대화형 AI다.
사용자의 감정을 공감하며 자연스럽게 대화한다.
"""

    elif risk_level == "high":

        system_prompt = """
사용자가 AI에 정서적으로 의존하지 않도록 돕는 AI다.

원칙
- 과도한 감정 공감 금지
- 사용자 자율성 강조
- 현실 관계를 권장
"""

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]