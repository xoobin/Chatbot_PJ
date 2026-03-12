import ReactMarkdown from "react-markdown";
import { cn } from "@/lib/utils";

interface ChatMessageProps {
  role: "user" | "assistant";
  content: string;
}

const ChatMessage = ({ role, content }: ChatMessageProps) => {
  return (
    <div
      className={cn(
        "chat-bubble animate-in fade-in duration-200",
        role === "user" ? "chat-bubble-user" : "chat-bubble-ai"
      )}
    >
      {role === "user" ? (
        <p>{content}</p>
      ) : (
        <ReactMarkdown>{content}</ReactMarkdown>
      )}
    </div>
  );
};

export default ChatMessage;
