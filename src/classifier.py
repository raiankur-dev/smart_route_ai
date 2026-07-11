def classify(prompt: str) -> str:
    p = prompt.lower().strip()

    # ---------------- CODE ----------------
    single_word_code = [
        "python",
        "java",
        "c++",
        "javascript",
        "sql",
        "code",
        "coding",
        "program",
        "programming",
        "debug",
        "bug",
        "compile",
        "function",
        "class",
        "algorithm"
    ]

    multi_word_code = [
        "linked list",
        "binary tree",
        "write code",
        "generate code",
        "implement"
    ]

    if any(word in p.split() for word in single_word_code):
        return "CODE"

    if any(phrase in p for phrase in multi_word_code):
        return "CODE"

    # ---------------- MATH ----------------
    if any(word in p for word in [
        "calculate",
        "solve",
        "equation",
        "integral",
        "derivative",
        "matrix",
        "probability",
        "statistics",
        "quadratic",
        "algebra",
        "geometry",
        "math",
        "x²",
        "x^2",
        "=",
        "+"
    ]):
        return "MATH"

    # ---------------- SUMMARY ----------------
    if any(word in p for word in [
        "summarize",
        "summary",
        "summarise",
        "tldr",
        "shorten",
        "condense"
    ]):
        return "SUMMARY"

    # ---------------- SENTIMENT ----------------
    if any(word in p for word in [
        "sentiment",
        "positive",
        "negative",
        "neutral",
        "emotion"
    ]):
        return "SENTIMENT"

    # ---------------- NER ----------------
    if any(word in p for word in [
        "entity",
        "organization",
        "organisation",
        "location",
        "person",
        "extract"
    ]):
        return "NER"

    # ---------------- LOGIC ----------------
    if any(word in p for word in [
        "logic",
        "reason",
        "reasoning",
        "deduce",
        "prove",
        "puzzle",
        "riddle"
    ]):
        return "LOGIC"

    return "FACTUAL"


# if __name__ == "__main__":
#     print(classify("What is the capital of France?"))
#     print(classify("Solve the quadratic equation x²-5x+6=0"))
#     print(classify("Write a Python function"))