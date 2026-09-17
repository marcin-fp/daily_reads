"""List all models available on AWS Bedrock."""
import boto3

bedrock = boto3.client("bedrock", region_name="us-east-1")

response = bedrock.list_foundation_models()

for model in response["modelSummaries"]:
    print(model["modelId"], "-", model["modelName"])


"""List all models available on OpenAI."""
from openai import OpenAI

client = OpenAI()

for model in client.models.list().data:
    print(model.id)