export default function MessageBubble({ role, text }) {
  return (
    <div className={role === "user" ? "msg user" : "msg bot"}>
      <strong>{role === "user" ? "You" : "Bot"}:</strong>
      <p>{text}</p>
    </div>
  );
}