import openai
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

gpt = OpenAI(
    api_key=os.getenv("API_KEY")
)

user_input = input("Enter your prompt here: ")

response = gpt.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": user_input
        }
    ]
)

print(response.choices[0].message.content)

