"""Minimal example to make a call to one of the models hosted on AWS."""
import boto3

client = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1",
)

response = client.converse(
    modelId="global.anthropic.claude-sonnet-5",
    messages=[
        {
            "role": "user",
            "content": [
                {"text": "What is machine learning?"}
            ],
        }
    ],
    inferenceConfig={
        "maxTokens": 1024,
    },
)

print(response["output"]["message"]["content"][0]["text"])