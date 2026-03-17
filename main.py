import sys
from prompts import build_prompt
from llm_client import ask_llm


def print_divider():
    print("-" * 50)


def print_examples(examples):
    if not examples:
        print("例句：無")
        return

    print("例句：")
    for i, example in enumerate(examples, 1):
        en = example.get("en", "").strip()
        zh = example.get("zh", "").strip()

        print_divider()
        print(f"{i}.")
        print(f"EN: {en}")
        print(f"ZH: {zh}")


def print_result(data):
    word = data.get("word", "")
    part_of_speech = data.get("part_of_speech", "")
    ipa = data.get("ipa", "")
    english_meaning = data.get("english_meaning", [])
    chinese_meaning = data.get("chinese_meaning", [])
    examples = data.get("examples", [])

    print()
    print("📘 單字練習小助手")
    print_divider()
    print(f"單字：{word}")
    print(f"詞性：{part_of_speech}")
    print(f"音標：{ipa}")
    print()

    print("英文意思：")
    if english_meaning:
        for i, meaning in enumerate(english_meaning, 1):
            print(f"{i}. {meaning}")
    else:
        print("無")
    print()

    print("中文意思：")
    if chinese_meaning:
        for i, meaning in enumerate(chinese_meaning, 1):
            print(f"{i}. {meaning}")
    else:
        print("無")
    print()

    print_examples(examples)
    print()
    print_divider()


def main():
    if len(sys.argv) < 2:
        print("請輸入一個英文單字，例如：python main.py discipline")
        return

    user_input = " ".join(sys.argv[1:])
    prompt = build_prompt(user_input)

    try:
        result = ask_llm(prompt)
        print_result(result)
    except Exception as e:
        print()
        print("❌ 執行失敗")
        print_divider()
        print(str(e))
        print_divider()


if __name__ == "__main__":
    main()