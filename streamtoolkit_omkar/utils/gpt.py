import openai
from ..config.env import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def probe_and_summarize(description):
    messages = [
        {"role": "system", "content": "You are a property issue summarizer."},
        {"role": "user", "content": description}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4-0125-preview",
        messages=messages,
        temperature=0.4
    )
    return {
        "summary": response["choices"][0]["message"]["content"],
        "raw_input": description
    }
