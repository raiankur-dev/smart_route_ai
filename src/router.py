from classifier import classify
from local_model import ask_local
from fireworks_client import ask_fireworks,get_remote_model

LOCAL_MODEL = "LOCAL"
REMOTE_MODEL = "REMOTE"

def route(prompt):

    decision = route_prompt(prompt)

    print("="*60)
    print(f"Task: {decision['task']}")
    print(f"Complexity: {decision['complexity']}")
    print(f"Model: {decision['model']}")

    for r in decision["reason"]:
        print("-", r)

    print("="*60)

    if decision["model"] == LOCAL_MODEL:

        answer = ask_local(prompt)

        # Automatic fallback
        if (
            len(answer.strip()) < 20
            or "i don't know" in answer.lower()
            or "cannot answer" in answer.lower()
            or "not sure" in answer.lower()
        ):
            print("Fallback -> Fireworks")
            return ask_fireworks(prompt)

        return answer

    return ask_fireworks(prompt)
    
def route_prompt(prompt: str):
    """
    Decide whether to use the local model or remote model.
    Returns:
        model_name,
        task_type,
        complexity_score,
        reasoning
    """

    task, scores = classify(prompt)

    complexity = 0
    reasons = []

    # -----------------------------
    # Complexity based on task
    # -----------------------------

    if scores["CODE"] > 0:
        complexity += 4
        reasons.append("Programming task detected")

    if scores["MATH"] > 0:
        complexity += 4
        reasons.append("Mathematical reasoning detected")

    if scores["LOGIC"] > 0:
        complexity += 3
        reasons.append("Complex reasoning/explanation detected")

    if scores["SUMMARY"] > 0:
        complexity += 1
        reasons.append("Summarization task")

    if scores["NER"] > 0:
        complexity += 1
        reasons.append("Named Entity Recognition")

    if scores["SENTIMENT"] > 0:
        complexity += 1
        reasons.append("Sentiment analysis")

    # -----------------------------
    # Prompt length
    # -----------------------------

    word_count = len(prompt.split())

    if word_count > 200:
        complexity += 3
        reasons.append("Very long prompt")

    elif word_count > 120:
        complexity += 2
        reasons.append("Long prompt")

    elif word_count > 60:
        complexity += 1
        reasons.append("Moderately long prompt")

    # -----------------------------
    # Formatting constraints
    # -----------------------------

    formatting_words = [
        "exactly",
        "bullet",
        "json",
        "table",
        "csv",
        "markdown",
        "step by step",
        "strictly"
    ]

    lower = prompt.lower()

    for word in formatting_words:
        if word in lower:
            complexity += 2
            reasons.append(f"Formatting constraint ({word})")
            break

    # -----------------------------
    # Final decision
    # -----------------------------

    # Always send code and math to DeepSeek
    if task in ["CODE", "MATH"]:
        model = REMOTE_MODEL

    elif complexity >= 5:
        model = REMOTE_MODEL

    else:
        model = LOCAL_MODEL

    return {
        "model": model,
        "task": task,
        "complexity": complexity,
        "reason": reasons if reasons else ["Simple factual task"],
        "remote_model": get_remote_model()
    }