import os
from openai import OpenAI

def generate_response(prompt):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "OpenAI API key not configured."

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
