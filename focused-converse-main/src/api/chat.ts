//API 통신만 담당하는 곳
export async function sendMessage(message: string) {

  const res = await fetch("https://chatbot-pj-2026.onrender.com/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
    user_id: "user1",
    message
})
  });

  const data = await res.json();

  return data.response;
}
