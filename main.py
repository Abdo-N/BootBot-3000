import os
from dotenv import load_dotenv
from openai import OpenAI

#loading API key from .env
load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key == None:
    raise RuntimeError("API key not found")

#connecting
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)



def main():
    response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
        }
    ])

    if response.usage == None:
        raise RuntimeError("Response usage property is None")
    else:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
        print(f"Response: {response.choices[0].message.content}")


if __name__ == "__main__":
    main()
