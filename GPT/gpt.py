import time
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv
import os

load_dotenv()

gpt = OpenAI(
    api_key=os.getenv("API_KEY")
)
continue_prompt = True

while continue_prompt:
    user_input = input("Enter your prompt here. "
                       "If you want to end this program, enter 'Y': ")

    try:
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

        if user_input.lower() == "y":
            all_prompts = input("Do you want a record of all your prompts? "
                                "If yes, enter 'Y', if not, enter 'N' to close the program: ")

            if all_prompts.lower() == "y":
                response_dict = [{
                    "prompt": user_input,
                    "message": response.choices[0].message.content
                }]
                print(response_dict)

            time.sleep(2)

            print("Exiting program...")
            continue_prompt = False

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


