# 사용자 상태 저장

user_states = {}


def get_user_state(user_id):

    if user_id not in user_states:
        user_states[user_id] = {
            "mirroring_count": 0,
            "message_count": 0,
            "dependency_score": 0,
            "lambda_value": 0.85,
            "risk_level": "low"
        }

    return user_states[user_id]