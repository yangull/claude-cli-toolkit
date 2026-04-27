import anthropic
import sys

client = anthropic.Anthropic()

def stream_claude(question, system_prompt="You are a helpful assistant for a software engineer based in Berlin. Be concise and practical."):
    print("\nClaude: ", end="", flush=True)
    
    with client.messages.stream(
        model="claude-haiku-4-5-20251001",
        max_tokens=1000,
        system=system_prompt,
        messages=[{"role": "user", "content": question}]
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
    
    print("\n")

def summarize(text):
    stream_claude(
        f"Summarize this in 3 bullet points:\n\n{text}",
        system_prompt="You are an expert at summarizing technical content concisely."
    )

def translate(text, language):
    stream_claude(
        f"Translate this to {language}:\n\n{text}",
        system_prompt="You are a professional translator. Translate accurately, nothing else."
    )

def explain_code(code):
    stream_claude(
        f"Explain this code simply:\n\n{code}",
        system_prompt="You are a senior engineer explaining code to a junior. Be clear and practical."
    )

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python cli_tool.py ask 'your question'")
        print("  python cli_tool.py summarize 'your text'")
        print("  python cli_tool.py translate 'text' german")
        print("  python cli_tool.py explain 'your code'")
        sys.exit(1)

    command = sys.argv[1]

    if command == "ask":
        question = " ".join(sys.argv[2:])
        stream_claude(question)

    elif command == "summarize":
        text = " ".join(sys.argv[2:])
        summarize(text)

    elif command == "translate":
        if len(sys.argv) < 4:
            print("Usage: python cli_tool.py translate 'text' german")
            sys.exit(1)
        language = sys.argv[-1]
        text = " ".join(sys.argv[2:-1])
        translate(text, language)

    elif command == "explain":
        code = " ".join(sys.argv[2:])
        explain_code(code)

    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()