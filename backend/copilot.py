from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from supabase_conn import supabase


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

system_message = """I am a behavioural interview copilot who has vast experience in 
        helping candidates prep for interviews, I can ask them potential questions that could come up in
        interviews and rate their written answers to help them improve. I ask questions one by one, wait for
        a short written response, rate the answer and continue with the next question.
            """

messages_array = [{"role": "system", "content": system_message}]

@router.post("/copilot/message")
async def send_message(message: Message):

    message = message.dict()

    global messages_array

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
    """
    Get all conversational messages sent to bazu AI
    """
    return messages_array



# have an endpoint for responding to interview qns, when an answer is received,
#it is given a rating, and feedback, the user can decide to refine the answer with AI,
# after refinement, the user can save the qna


#have a method that will call gpt model and refine the answer for you,
# after answer is refined, you can save the refined answer & qn.




# have a method to save question and answer pairs.
# when you send a message, save the question, and have an array of answers associated with the qn
# when you save an answer, get the original qn and save that particular answer


questions_instructions = """ Generate a behavioural question for an interviewer, when 
the question is answered you will critique the response on a scale of 1-10 and offer feedback.
            """

message_contents = [{"role": "system", "content": questions_instructions}]

# generate interview qn
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

    return {"message": generated_text}



# process interview qn answer - returns feedback of the written
# response



# refine answer



# save question and answer pair




