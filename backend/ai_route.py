import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq
import json
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv('GROQ_API_KEY'),
)

MODEL = 'llama-3.3-70b-versatile'

# initialize FastAPI
app = FastAPI()

# define class for the request body
# Define Pydantic model for incoming user messages
class UserMessage(BaseModel):
    message: str

messages=[
            {
                'role': 'system',
                'content': 'You are a helpful medical assistant that can help diagnose an issue the user describes. You will have a back and forth conversation with the use asking one question at a time, in a natural tone. you do not have to summarize everything the use tells you but do mention th eimportant things. Then ask your next question but ask it in a new line. Ask consise questions, do not repeat yourself, only ask the important questions. Once you have gathered information to form a diagnosis, you will provide the user with a diagnosis. If a user asks you to verify a possible diagnosis, verify it and end your diagnosis with by describing why it is possible that the user is rigth or wrong.'
            }
]

@app.post('/api/docai')
async def doc_ai_diagnosis(inquiry: UserMessage):
    """
    API endpoint to interact with the medical assistant.
    """
    try:
        # Append the user's message to the conversation
        messages.append({
            'role': 'user',
            'content': inquiry.message
        })

        chat_completion = client.chat.completions.create(
            model=MODEL,
            messages=messages,
        )

        # Get the assistant's response
        assistant_response = chat_completion.choices[0].message.content

        # Append the assistant's response to the conversation
        messages.append({
            'role': 'assistant',
            'content': assistant_response
        })

        if "diagnosis" in assistant_response.lower() or "recommend" in assistant_response.lower():
            return {"message": assistant_response, "diagnosis_complete": True}

        return {"message": assistant_response, "diagnosis_complete": False}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


