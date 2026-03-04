import json
from google import genai
from config import MODEL

client = genai.Client()

def ask_llm(prompt: str):
    response = client.models.generate_content(
        model=MODEL, 
        contents=prompt
    )
    clean_text = response.text.replace("```json", "").replace("```", "").strip()
    data = json.loads(clean_text)

    return data
