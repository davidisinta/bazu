
"""This module contains all code that involves the ai copilot, from speaking to the
Azure AI service, to communicating with the database."""


from fastapi import APIRouter
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

import supabase_conn


router = APIRouter()


def main():
    try:

        # Get configuration settings
        load_dotenv()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")

        # Initialize the Azure OpenAI client
        client = AzureOpenAI(
            azure_endpoint=azure_oai_endpoint,
            api_key=azure_oai_key,
            api_version="2024-02-15-preview"
        )

        # Create a system message
        system_message = """I am a behavioural interview copilot who has vast experience in 
        helping candidates prep for interviews, I can ask them potential questions that could come up in
        interviews and rate their written answers to help them improve. I ask questions one by one, wait for
        a short written response, rate the answer and continue with the next question.
            """

        # Initialize messages array
        messages_array = [{"role": "system", "content": system_message}]

        while True:
            # Get input text
            input_text = input("Enter the prompt (or type 'quit' to exit): ")
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue

            print("\nSending request for summary to Azure OpenAI endpoint...\n\n")

            # Add code to send request...
            # Send request to Azure OpenAI model
            messages_array.append({"role": "user", "content": input_text})

            response = client.chat.completions.create(
                model=azure_oai_deployment,
                temperature=0.7,
                max_tokens=1200,
                messages=messages_array
            )


            generated_text = response.choices[0].message.content
            # Add generated text to messages array
            messages_array.append({"role": "assistant", "content": generated_text})

            # Print generated text
            print("Summary: " + generated_text + "\n")



    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()


@router.get("/copilot/")
async def read_items():
    return [{"item_id": "item1, here we go"}, {"item_id": "item2"}]

@router.get("/copilot/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id}


