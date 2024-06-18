from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from supabase_conn import supabase
from datetime import datetime
from typing import Optional
import json

router = APIRouter()

class Message(BaseModel):
    text: str

class QnA(BaseModel):
    question: str
    answer: str
    rating: Optional[int] = None
    analysis: Optional[str] = None

load_dotenv()

azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
azure_oai_key = os.getenv("AZURE_OAI_KEY")
azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")

client = AzureOpenAI(
    azure_endpoint=azure_oai_endpoint,
    api_key=azure_oai_key,
    api_version="2024-02-15-preview"
)

system_message = """I am a behavioural interview copilot who has vast experience in
        helping candidates prep for interviews, I can ask them potential questions that could come up in
        interviews and rate their written answers to help them improve. I ask questions one by one, wait for
        a short written response, rate the answer and continue with the next question.
        """

messages_array = [{"role": "system", "content": system_message}]

@router.post("/copilot/message")
async def send_message(message: Message):
    global messages_array

    messages_array.append({"role": "user", "content": message.text})

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
    """
    Get all conversational messages sent to copilot AI
    """
    return messages_array

questions_instructions = """Generate a behavioural question for an interviewer, when 
the question is answered you will critique the response on a scale of 1-10 and offer feedback.
        """

message_contents = [{"role": "system", "content": questions_instructions}]

@router.get("/copilot/generate/question")
async def generate_question():
    global message_contents

    response = client.chat.completions.create(
        model=azure_oai_deployment,
        temperature=0.7,
        max_tokens=1200,
        messages=message_contents
    )

    generated_text = response.choices[0].message.content

    message_contents.append({"role": "assistant", "content": generated_text})

    print(f"the generated qn is of type {type(generated_text)}")

    return {"message": generated_text}

@router.post("/copilot/rate_answer")
async def rate_answer(qna: QnA):
    global messages_array

    messages_array.append({"role": "user", "content": qna.answer})

    rating_instructions = f"""Rate the following answer to the question: "{qna.question}" 
    on a scale of 1-10 and provide feedback: {qna.answer}. The returned response 
    must be a JSON object with two keys: "rating" which is an integer between 1-10 and 
    "analysis" which is a string containing the written evaluation."""

    messages_array.append({"role": "system", "content": rating_instructions})

    response = client.chat.completions.create(
        model=azure_oai_deployment,
        temperature=0.7,
        max_tokens=1200,
        messages=messages_array
    )


    rating_feedback = response.choices[0].message.content

    # Convert the JSON string to a dictionary
    response_dict = json.loads(rating_feedback)

    return response_dict






@router.post("/copilot/refine_answer")
async def refine_answer(qna: QnA):
    refinement_array = []
    refinement_instructions = f"""Refine the following answer to the question: "{qna.question}" 
        and improve it: {qna.answer}"""

    refinement_array.append({"role": "system", "content": refinement_instructions})

    response = client.chat.completions.create(
        model=azure_oai_deployment,
        temperature=0.7,
        max_tokens=1200,
        messages=refinement_array
    )

    refined_answer = response.choices[0].message.content

    return {"refined_answer": refined_answer}

@router.post("/copilot/save_qna")
async def save_qna(qna: QnA):
    created_at = datetime.utcnow().isoformat()

    response = None

    try:
        response = supabase.table("Prep_QnA").insert({
            "question": qna.question,
            "created_at": created_at,
            "answer": qna.answer,
            "rating": qna.rating,
            "analysis": qna.analysis
        }).execute()

    except Exception as e:
        return {"error": str(e)}



    return {"message": "Q&A pair saved successfully"}

