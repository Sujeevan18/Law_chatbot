from openai import OpenAI
from app.config import OPENAI_API_KEY, OPENAI_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)


def build_context(results):
    parts = []
    for i, item in enumerate(results, start=1):
        parts.append(
            f"[Source {i}: {item['source']} | chunk {item['chunk_id']} | score={item['score']:.4f}]\n{item['text']}"
        )
    return "\n\n".join(parts)


def generate_answer(question: str, results):
    context = build_context(results)

    system_prompt = """
You are a legal information assistant for Sri Lankan law.
Answer only using the provided legal context.
Do not invent laws, sections, or legal conclusions.
If the context is insufficient, say you could not find a reliable answer.
Always mention that the answer is not legal advice.
"""

    user_prompt = f"""
Question:
{question}

Legal Context:
{context}

Return JSON-style plain text answer with:
1. direct answer
2. supporting sources
3. disclaimer
"""

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        temperature=0.1,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    return response.choices[0].message.content