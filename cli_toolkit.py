import anthropic
import sys

def ask_claude(question):
    client = anthropic.Anthropic()
    
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1000,
        system="You are a senior Berlin software engineer. Give extremely blunt, short answers. No fluff, no politeness. Just the facts.",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    
    return response.content[0].text

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli_tool.py 'your question here'")
        sys.exit(1)
    
    question = " ".join(sys.argv[1:])
    answer = ask_claude(question)
    print(f"\nClaude: {answer}\n")

if __name__ == "__main__":
    main()