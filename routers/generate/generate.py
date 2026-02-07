from fastapi import APIRouter
from pydantic import BaseModel
from google import genai
from google.genai import types
from .prompts import *
from dotenv import load_dotenv
import os

load_dotenv()
router = APIRouter()

class Request(BaseModel):
    input: str


@router.post("/generate")
async def generate(request: Request):

    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-3-flash-preview"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=PROMPT),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=request.input),
            ],
        ),
    ]
    tools = [
        types.Tool(code_execution=types.ToolCodeExecution),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="HIGH",
        ),
        tools=tools,
    )

    response = client.models.generate_content(
        model = model,
        contents = contents,
        config = generate_content_config
    )
    result = ''
    if response.parts[0].text:
        result += response.parts[0].text
    if response.parts[0].executable_code:
        result += response.parts[0].executable_code
    if response.parts[0].code_execution_result:
        result += response.parts[0].code_execution_result

    return {
        'output': result
    }

