import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # fast + cheap + powerful
        messages=[
            {"role": "system", "content": "You are a smart AI assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    answer = response.choices[0].message.content
    return answer
