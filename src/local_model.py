from transformers import pipeline

print("Loading Qwen Local Model...")

pipe = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct",
    device_map="auto"
)

print("Qwen Loaded Successfully")


def ask_local(prompt: str):

    output = pipe(
        prompt,
        max_new_tokens=64,
        do_sample=False,
        return_full_text=False
    )

    return output[0]["generated_text"]