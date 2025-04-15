import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize the OpenAI client with the API key
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def query_llm(prompt):
    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            instructions="You are an experienced security expert providing clear and actionable advice.",
            input=prompt,
            temperature=0.7,
        )
        return response.output_text.strip()
    except Exception as e:
        print("LLM query error:", e)
        return "An error occurred while querying the LLM."