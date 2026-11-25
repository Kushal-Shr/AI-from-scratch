import os
import anthropic

client = anthropic.Anthropic()

MODEL = os.environ.get("LLM_MODEL", "claude-haiku-5-5")

msg = input("Enter your message: ")

response = client.messages.create(
    model = MODEL,
    max_tokens = 256,
    messages = [
        {
            "role": "user",
            "content": msg
        }
    ]
)

print("AI: ", response.content[0].text)