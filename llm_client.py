import os
import json
from openai import OpenAI


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def clean_json_text(text: str) -> str:
    if not text:
        return ""

    text = text.strip()

    if text.startswith("```json"):
        text = text[len("```json"):].strip()
    elif text.startswith("```"):
        text = text[len("```"):].strip()

    if text.endswith("```"):
        text = text[:-3].strip()

    return text


def ask_llm(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )

    raw_text = response.choices[0].message.content or ""
    clean_text = clean_json_text(raw_text)

    if not clean_text:
        raise ValueError("AI 沒有回傳內容，請稍後再試一次。")

    try:
        return json.loads(clean_text)
    except json.JSONDecodeError:
        raise ValueError(
            f"AI 回傳的內容不是有效 JSON。\n\n原始回傳內容：\n{raw_text}"
        )