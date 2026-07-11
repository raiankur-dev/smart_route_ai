from classifier import classify
from fireworks_client import ask_fireworks
from local_model import ask_local

REMOTE_TASKS = {
    "CODE",
    "LOGIC",
    "MATH"
}

LOCAL_TASKS = {
    "FACTUAL",
    "NER",
    "SENTIMENT"
}


def route(prompt):

    task = classify(prompt)

    print("=" * 50)
    print(f"Task Type : {task}")

    # Always remote
    if task in REMOTE_TASKS:
        print("Decision : REMOTE")
        return ask_fireworks(prompt)

    # Long summaries
    if task == "SUMMARY":
        if len(prompt) > 300:
            print("Decision : REMOTE")
            return ask_fireworks(prompt)

    print("Decision : LOCAL")

    return ask_local(prompt)