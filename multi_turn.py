import anthropic

client = anthropic.Anthropic()

messages = []

print("Chat with Claude (type 'quit' to exit)")
print("-" * 40)

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        break
    
    messages.append({
        "role": "user",
        "content": user_input
    })
    
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1000,
        system="You are a helpful assistant for a software engineer learning to build AI tools in Berlin.",
        messages=messages
    )
    
    assistant_message = response.content[0].text
    
    messages.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    print(f"Claude: {assistant_message}")
    print()