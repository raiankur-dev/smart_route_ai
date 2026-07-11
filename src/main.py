import json
from pathlib import Path

from router import route

INPUT_FILE = Path("input/tasks.json")
OUTPUT_FILE = Path("output/results.json")


def main():

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        tasks = json.load(f)

    results = []

    print(f"Loaded {len(tasks)} tasks")

    for task in tasks:

        print(f"\nProcessing {task['task_id']}")

        answer = route(task["prompt"])

        results.append(
            {
                "task_id": task["task_id"],
                "answer": answer
            }
        )

    OUTPUT_FILE.parent.mkdir(exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    print("\nFinished Successfully")


if __name__ == "__main__":
    main()