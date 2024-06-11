from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import supabase_conn


router = APIRouter()


class Message(BaseModel):
    text: str


load_dotenv()

azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
azure_oai_key = os.getenv("AZURE_OAI_KEY")
azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")

client = AzureOpenAI(
    azure_endpoint=azure_oai_endpoint,
    api_key=azure_oai_key,
    api_version="2024-02-15-preview"
)

messages_array = []


@router.post("/copilot/message")
async def send_message(message: Message):

    message = message.dict()

    global messages_array
    if message["text"].lower() == "quit":
        messages_array = []
        return {"message": "Conversation ended. Start a new conversation by sending a message."}
    if len(message["text"]) == 0:
        return {"message": "Please enter a prompt."}

    messages_array.append({"role": "user", "content": message["text"]})

    response = client.chat.completions.create(
        model=azure_oai_deployment,
        temperature=0.7,
        max_tokens=1200,
        messages=messages_array
    )

    generated_text = response.choices[0].message.content
    messages_array.append({"role": "assistant", "content": generated_text})

    return {"message": generated_text}


@router.get("/copilot/messages")
async def get_messages():
    return messages_array


