import { useState } from "react";
import { sendMessage, indexDocuments } from "../api/chatApi";
import MessageBubble from "./MessageBubble";
import SourceList from "./SourceList";

export default function ChatBox() {
  const [messages, setMessages] = useState([]);
  const [question, setQuestion] = useState("");
  const [sources, setSources] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleIndex = async () => {
    setLoading(true);
    try {
      const res = await indexDocuments();
      alert(res.message + ` (${res.total_documents} docs, ${res.total_chunks} chunks)`);
    } catch (err) {
      alert("Failed to index documents");
    }
    setLoading(false);
  };

  const handleSend = async () => {
    if (!question.trim()) return;

    const userMessage = { role: "user", text: question };
    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);

    try {
      const res = await sendMessage(question);

      const botMessage = { role: "bot", text: res.answer };
      setMessages((prev) => [...prev, botMessage]);
      setSources(res.sources);
    } catch (err) {
      const botMessage = { role: "bot", text: "Error while getting response." };
      setMessages((prev) => [...prev, botMessage]);
    }

    setQuestion("");
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>Sri Lankan Law Chatbot</h1>

      <button onClick={handleIndex} disabled={loading}>
        {loading ? "Processing..." : "Index Legal Documents"}
      </button>

      <div className="chat-window">
        {messages.map((msg, index) => (
          <MessageBubble key={index} role={msg.role} text={msg.text} />
        ))}
      </div>

      <div className="input-row">
        <input
          type="text"
          value={question}
          placeholder="Ask about Sri Lankan law..."
          onChange={(e) => setQuestion(e.target.value)}
        />
        <button onClick={handleSend} disabled={loading}>
          Send
        </button>
      </div>

      <SourceList sources={sources} />
    </div>
  );
}