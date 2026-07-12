import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

import os
import streamlit as st
from openai import OpenAI

api_key = os.getenv("FIREWORKS_API_KEY")

if not api_key:
    api_key = st.secrets["FIREWORKS_API_KEY"]

client = OpenAI(
    api_key=api_key,
    base_url="https://api.fireworks.ai/inference/v1"
)


def ask_fireworks(prompt: str):

    response = client.chat.completions.create(
        model=os.getenv(
            "REMOTE_MODEL",
            "accounts/fireworks/models/deepseek-v4-pro"
        ),
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content