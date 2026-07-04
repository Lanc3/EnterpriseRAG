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
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        stream=False,
    )

    return completion.choices[0].message.content.strip()


def evaluate_generated_answer(expected_answer: str, generated_answer: str) -> str:
    prompt = f"""
You are evaluating a RAG system answer.

Return your response in this exact format:

RESULT: PASS or FAIL
REASON: explain why the answer passed or failed

Evaluation rules:
- PASS if the generated answer gives the same core information as the expected answer.
- FAIL if the generated answer is missing important information, is wrong, or is too vague.
- Do not be overly strict about wording.
- Judge meaning, not exact phrasing.

Expected answer:
{expected_answer}

Generated answer:
{generated_answer}
"""

    response = send_to_deepseek(prompt)
    return response.strip()