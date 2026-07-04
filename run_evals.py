import os
from dotenv import load_dotenv
import openai

load_dotenv()

client = openai(
    api_key = os.environ.get("DEEPSEEK_API_KEY"),
    BASE_URL = "https://api.deepseek.com",
)

def send_to_deepseek(message :str) -> str:
    completion = client.chat.completion.create(
        model="deepseek-v4-flash",
        messages=[{"role":"user","content":message}],
        stream=False,
        extra_body={"thinking":{"type":"disabled"}},
    )
    return completion.choices[0].message.content.strip()

def evaluate_generated_answer(expected_answer,generated_answer):
    prompt=f'''Please evaluate the generated answer.
        -If the generated answer provides the same information as the expected answer, then return PASS . Otherwise return FAIL. 
        Expected answer:{expected_answer}
        Generated answer:{generated_answer}'''
    response = send_to_deepseek(prompt)    
    return response



test = "string"