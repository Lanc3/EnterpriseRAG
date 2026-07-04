import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

def send_to_deepseek(message: str) -> str:
    completion = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": message}],
        stream=False,
    )
    return completion.choices[0].message.content.strip()

def evaluate_generated_answer(expected_answer, generated_answer):
    prompt = f"""Please evaluate the generated answer.
If the generated answer provides the same information as the expected answer, return PASS.
Otherwise return FAIL.

Expected answer: {expected_answer}
Generated answer: {generated_answer}
"""
    response = send_to_deepseek(prompt)
    return response.strip()