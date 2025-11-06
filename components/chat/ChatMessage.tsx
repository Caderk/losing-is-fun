import { Message } from "@/lib/types/chat";

interface ChatMessageProps {
  message: Message;
}

export default function ChatMessage({ message }: ChatMessageProps) {
  const isUser = message.role === "user";

  return (
    <div className={`mb-8 flex ${isUser ? "justify-end" : "justify-start"}`}>
      <div
        className={`flex gap-3 max-w-4xl ${isUser ? "flex-row-reverse" : "flex-row"}`}
      >
        {/* Avatar Badge */}
        <div
          className={`flex-shrink-0 w-10 h-10 rounded-full flex items-center justify-center text-white font-semibold ${
            isUser ? "bg-blue-600" : "bg-gray-600"
          }`}
        >
          {isUser ? "U" : "A"}
        </div>

        {/* Message Content */}
        <div
          className={`px-4 py-3 rounded-lg ${
            isUser
              ? "bg-gradient-to-r from-blue-500 to-blue-600 text-white"
              : "bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-gray-100"
          }`}
        >
          <div className="whitespace-pre-wrap break-words">
            {message.content}
          </div>
        </div>
      </div>
    </div>
  );
}
