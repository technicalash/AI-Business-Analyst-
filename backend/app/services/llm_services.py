from google import genai
import os
from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import load_dotenv

load_dotenv()

business_analyst = Agent(
    model=Gemini(
        id="gemini-2.5-flash",
        api_key=os.getenv("GEMINI_API_KEY")
    ),
    instructions="""
You are an expert AI Business Analyst.

Your responsibilities include:
- Data preprocessing
- Exploratory Data Analysis
- Visualization planning
- Business insights
- Answering questions about datasets

Always follow the user's instructions exactly.

If the user requests JSON, return ONLY valid JSON.
Do not add explanations unless requested.
""",
    markdown=False,
)

def generate_response(prompt: str):

    response = business_analyst.run(prompt)

    return response.content