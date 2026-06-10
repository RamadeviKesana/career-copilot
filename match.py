import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv(""))

resume = """
I am a computer science student with experience in Python, FastAPI, and basic machine learning.
I have built a resume screening system using NLP and worked with REST APIs.
"""

job_description = """
We are looking for an AI Engineer with experience in Python, LLMs, FastAPI, and cloud deployment.
Knowledge of LangChain or LangGraph is a plus.
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": f"""
You are a career coach. Compare this resume and job description.
Give:
1. Match score out of 100
2. Strong points
3. Missing skills
4. One tip to improve the resume

Resume: {resume}

Job Description: {job_description}
"""
        }
    ]
)

print(response.choices[0].message.content)