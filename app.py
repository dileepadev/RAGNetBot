import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

deployment_name = "gpt-35-turbo-instruct"

# Send a completion call to generate an answer
print("Sending a test completion job")
start_phrase = "Write a welcome note for the RAGNetBot Chat service."
response = client.completions.create(
    model=deployment_name, prompt=start_phrase, max_tokens=200
)
print(start_phrase + response.choices[0].text)
