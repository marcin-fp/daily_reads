from openai import OpenAI

client = OpenAI()  # reads OPENAI_API_KEY from the environment

response = client.responses.create(
    model="gpt-5.6-luna",
    input="What is machine learning?",
    reasoning={
        "effort": "medium",
    },
    max_output_tokens=1024,
)

print(response.output_text)