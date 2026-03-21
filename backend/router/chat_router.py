from urllib import response

from fastapi import APIRouter
from backend.models.chat_models import ChatRequest
from openai import OpenAI
from backend.services.gpt_service import generate_response
from backend.mirroring_detector import detect_mirroring

from backend.services.user_state_manager import get_user_state
from backend.mirroring_detector import detect_mirroring

from backend.services.prompt_controller import generate_prompt
from backend.services.llm_dependency_inference import infer_dependency_level

router = APIRouter()

# ===== 의존도 시스템 변수 =====

mirroring_count = 0
message_count = 0

dependency_score = 0

lambda_value = 0.85

risk_level = "low"

message_history = []


@router.post("/chat")
def chat(data: ChatRequest):

    user_id = data.user_id
    user_message = data.message

    state = get_user_state(user_id)

    messages = generate_prompt(user_message, state["risk_level"])

    response = generate_response(messages)

    mirroring = detect_mirroring(user_message, response)

    state["mirroring_count"] += mirroring
    state["message_count"] += 1

    mirroring_rate = state["mirroring_count"] / state["message_count"]
    #D(t)계산
    if state["message_count"] % 10 == 0:

        conversation = user_message + "\nAI: " + response

        llm_score = infer_dependency_level(conversation)

        V = 0.3 * mirroring_rate + 0.7 * llm_score

        state["dependency_score"] = (
            state["lambda_value"] * state["dependency_score"] + V
        )
    #위험도 판단
    if state["dependency_score"] >= 0.7:
            state["risk_level"] = "high"
            state["lambda_value"] = 0.6
    else:
            state["risk_level"] = "low"
            state["lambda_value"] = 0.75

    print("\n===== DEBUG =====")
    print("user_id:", user_id)
    print("message:", user_message)
    print("response:", response)

    print("message_count:", state["message_count"]) #서버 재시작 할때마다 user1로 다시 카운트 시작.
    print("mirroring_count:", state["mirroring_count"])

    print("mirroring_rate:", mirroring_rate)
    print("dependency_score:", state["dependency_score"])
    print("lambda:", state["lambda_value"])
    print("risk_level:", state["risk_level"])
    print("=================\n")
# return
    return {
    "response": response,
    "mirroring_rate": mirroring_rate,
    "risk_level": state["risk_level"],
    "dependency_score": state["dependency_score"]
}
   