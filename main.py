import sys
from prompts import build_prompt
from llm_client import ask_llm


def main():
    # The client gets the API key from the environment variable `GEMINI_API_KEY`.

    if len(sys.argv) < 2:
        print("Please enter your prompt.")
        return
    
    user_input = " ".join(sys.argv[1:])
    prompt = build_prompt(user_input)
    result = ask_llm(prompt)
    print(result)


if __name__ == "__main__":
    main()