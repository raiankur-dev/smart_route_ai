import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

load_dotenv()

# ----------------------------
# API Key
# ----------------------------
api_key = os.getenv("FIREWORKS_API_KEY")

if not api_key:
    api_key = st.secrets["FIREWORKS_API_KEY"]

# ----------------------------
# Base URL
# ----------------------------
base_url = os.getenv(
    "FIREWORKS_BASE_URL",
    "https://api.fireworks.ai/inference/v1"
)

# ----------------------------
# Allowed Models
# ----------------------------
allowed_models = os.getenv("ALLOWED_MODELS")

if allowed_models:
    remote_model = allowed_models.split(",")[0].strip()
else:
    remote_model = os.getenv(
        "REMOTE_MODEL",
        "accounts/fireworks/models/deepseek-v4-pro"
    )

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)


def get_remote_model():
    return remote_model


def ask_fireworks(prompt: str):

    response = client.chat.completions.create(
        model=remote_model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content