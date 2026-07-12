from transformers import pipeline

print("Loading Qwen Local Model...")

pipe = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct",
    device_map="auto"
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