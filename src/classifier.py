import re

def classify(prompt: str):
    p = prompt.lower().strip()

    scores = {
        "CODE": 0,
        "MATH": 0,
        "SUMMARY": 0,
        "SENTIMENT": 0,
        "NER": 0,
        "LOGIC": 0,
        "FACTUAL": 0
    }

    # ---------------- CODE ----------------

    code_words = [
        "python","java","c++","javascript","sql",
        "function","class","algorithm","compile",
        "debug","bug","implement","linked list",
        "binary tree","write code","generate code"
    ]

    for word in code_words:
        if word in p:
            scores["CODE"] += 3

    # ---------------- MATH ----------------

    math_words = [
        "calculate","solve","equation",
        "integral","derivative",
        "matrix","probability",
        "statistics","quadratic",
        "geometry","algebra"
    ]

    for word in math_words:
        if word in p:
            scores["MATH"] += 3

    if re.search(r"\d+\s*[\+\-\*/]\s*\d+", p):
        scores["MATH"] += 3

    if re.search(r"x[\^²]?", p):
        scores["MATH"] += 2

    # ---------------- SUMMARY ----------------

    for word in [
        "summarize",
        "summarise",
        "summary",
        "tldr",
        "condense",
        "shorten"
    ]:
        if word in p:
            scores["SUMMARY"] += 3

    # ---------------- SENTIMENT ----------------

    for word in [
        "sentiment",
        "positive",
        "negative",
        "neutral",
        "emotion",
        "review"
    ]:
        if word in p:
            scores["SENTIMENT"] += 3

    # ---------------- NER ----------------

    for word in [
        "entity",
        "entities",
        "extract",
        "organization",
        "organisation",
        "location",
        "person",
        "date"
    ]:
        if word in p:
            scores["NER"] += 3

    # ---------------- LOGIC ----------------

    for word in [
        "why",
        "compare",
        "difference",
        "reason",
        "reasoning",
        "explain",
        "analyse",
        "analyze",
        "deduce",
        "puzzle",
        "riddle",
        "prove"
    ]:
        if word in p:
            scores["LOGIC"] += 2

    # Formatting requests are surprisingly difficult
    if "exactly" in p:
        scores["LOGIC"] += 2

    if "bullet" in p:
        scores["LOGIC"] += 2

    if "step by step" in p:
        scores["LOGIC"] += 2

    # Long prompts are generally harder
    if len(prompt.split()) > 120:
        scores["LOGIC"] += 2

    # If nothing else matches
    scores["FACTUAL"] = 1

    task = max(scores, key=scores.get)

    return task, scores