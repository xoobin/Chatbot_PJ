from openai import OpenAI
import os

def generate_response(messages):

    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message.content

    except Exception as e:
        print("GPT ERROR:", e)
        return "⚠️ 현재 AI 응답을 생성할 수 없습니다."
