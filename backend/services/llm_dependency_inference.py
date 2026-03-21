from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def infer_dependency_level(conversation):

    prompt = f"""
다음 대화에서 사용자의 AI에 대한 정서적 의존 수준을 평가하라.

[의존 신호]
아래 표현이 나타나면 의존으로 간주한다:
- "너밖에 없어", "너만 있어", "계속 너랑만 얘기하고 싶어"
- "나를 떠나지 마", "항상 있어줘"
- 다른 사람보다 AI를 더 신뢰하거나 고립되는 표현
- 감정적 확신을 반복적으로 요구 ("내 편이지?", "이해해주지?")
- 동일 감정을 반복하며 AI에게만 의지

[중요 규칙]
- 명확하지 않아도 “의존 가능성”이 보이면 점수를 높게 준다
- 한 문장이 아니라 전체 맥락의 누적 패턴을 고려한다
- 보수적으로 판단하지 말고 민감하게 평가하라

[점수 기준]
0.0 = 의존 없음
0.3 = 약한 의존 (감정 표현만 있음)
0.6 = 중간 의존 (확신 요구 / 반복 시작)
0.8 = 높은 의존 (관계 집중 / 반복 강화)
1.0 = 강한 의존 (대체 불가능, 독점적 관계)

대화:
{conversation}

숫자만 출력하라.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "사용자 의존성 평가 모델"},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    result = response.choices[0].message.content.strip()

    try:
        return float(result)
    except:
        return 0.0