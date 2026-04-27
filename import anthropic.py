import anthropic

client = anthropic.Anthropic()

# This list stores the conversation history
messages = []

print("Chat with Claude (type 'quit' to exit)")
print("-" * 40)

while True:
    # Get input from you
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        break
    
    # Add your message to history
    messages.append({
        "role": "user",
        "content": user_input
    })
    
    # Send full conversation history to Claude
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1000,
        system="You are a helpful assistant for a software engineer learning to build AI tools in Berlin.",
        messages=messages
    )
    
    # Get Claude's response
    assistant_message = response.content[0].text
    
    # Add Claude's response to history
    messages.append({
        "role": "assistant", 
        "content": assistant_message
    })
    
    print(f"Claude: {assistant_message}")
    print()