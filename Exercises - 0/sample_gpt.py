from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

azure_endpoint: str = os.environ.get('AZURE_ENDPOINT')
azure_openai_api_key: str = os.environ.get('AZURE_OPENAI_API_KEY')
azure_openai_api_version: str = os.environ.get('AZURE_OPENAI_API_VERSION')
azure_deployment: str = os.environ.get('AZURE_DEPLOYMENT')

client = AzureOpenAI(
    api_key=azure_openai_api_key,
    api_version=azure_openai_api_version,
    azure_endpoint = azure_endpoint
)

# Define a function to interact with gpt
def ask_gpt(prompt):
    try:
        # Call the OpenAI API to generate a response
      completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt
            }
          ]
        )

      return completion.choices[0].message.content

    except Exception as e:
        print(f"Error: {e}")
        return None

# Example prompt
user_prompt = "What is the capital of France?"

# Get GPT's response
gpt_response = ask_gpt(user_prompt)

# Print the response
print("GPT:", gpt_response)

