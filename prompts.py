BASE_PROMPT = """
You are a professional article summary assistant, 
please summariza the text user input, 
and output with json format as below：

{{
    "summary": "...",
    "keywords": ["", ""]
}}
"""

def build_prompt(user_input:str):
    return f"{BASE_PROMPT}\nUser input:\n{user_input}"