import openai
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

gpt = OpenAI(
    api_key=os.getenv("API_KEY")
)
continue_prompt = True

while continue_prompt:
    user_input = input("Enter your prompt here: .  If you want to stop prompts, or close the chatbot altogether, press Y.")

    response = gpt.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    if user_input == "y":
        continue_prompt = False

    print(response.choices[0].message.content)

