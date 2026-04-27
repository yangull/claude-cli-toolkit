import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Say hello and tell me one fact about Berlin"}
    ]
)

print(message.content[0].text)