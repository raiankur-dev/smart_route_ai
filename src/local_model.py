import os
import streamlit as st
from transformers import pipeline

# Try environment variable first (local)
hf_token = os.getenv("HF_TOKEN")

# If not found, try Streamlit Secrets
if not hf_token:
    try:
        hf_token = st.secrets["HF_TOKEN"]
    except Exception:
        hf_token = None

print("Loading Qwen Local Model...")

pipe = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct",
    device_map="auto",
    token=hf_token
)

print("Qwen Loaded Successfully")


def ask_local(prompt: str):

    messages = [
        {
            "role": "system",
            "content": (
                "You are a concise and accurate AI assistant.\n"
                "Answer ONLY what the user asks.\n"
                "Do not add extra sections.\n"
                "Do not generate JSON unless explicitly requested.\n"
                "Do not generate entities unless explicitly requested.\n"
                "Do not generate sentiment unless explicitly requested.\n"
                "Keep factual answers short.\n"
                "Follow formatting instructions exactly."
            )
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    output = pipe(
        messages,
        max_new_tokens=96,
        do_sample=False,
        return_full_text=False
    )

    return output[0]["generated_text"].strip()