#  Smart Route AI

A hybrid token-efficient routing agent built for the **AMD Developer Hackathon ACT II – Track 1**.

The project intelligently routes user prompts to either a **local lightweight LLM (Qwen 2.5 0.5B)** or a **remote high-performance LLM (DeepSeek V4 Pro via Fireworks AI)** based on the complexity of the task. The objective is to minimize remote token usage while maintaining high-quality responses.

---

##  Problem Statement

Large Language Models provide excellent performance but can be expensive due to token costs.

This project addresses that challenge by:

- Classifying incoming prompts
- Determining task complexity
- Executing simple tasks locally
- Routing complex tasks to a remote model

This hybrid approach reduces remote API usage while maintaining response quality.

---

##  Architecture

```
                 User Prompt
                      │
                      ▼
             Task Classifier
                      │
                      ▼
             Routing Decision
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
 Local Qwen 2.5 0.5B      DeepSeek V4 Pro
 (Runs Locally)          (Fireworks AI API)
          │                       │
          └───────────┬───────────┘
                      ▼
                 Final Response
```

---

##  Routing Strategy

The router classifies prompts into different categories and selects the most appropriate model.

| Task Type | Model Used |
|------------|------------|
| Factual Questions | Local Qwen |
| Short Summaries | Local Qwen |
| Named Entity Recognition | Local Qwen |
| Sentiment Analysis | Local Qwen |
| Code Generation | Remote DeepSeek |
| Mathematical Problems | Remote DeepSeek |
| Complex Reasoning | Remote DeepSeek |

The goal is to minimize remote inference while preserving answer quality.

---

## 📂 Project Structure

```
smart_route_ai/
│
├── src/
│   ├── main.py
│   ├── router.py
│   ├── classifier.py
│   ├── local_model.py
│   ├── fireworks_client.py
│   └── config.py
│
├── input/
│   └── tasks.json
│
├── output/
│   └── results.json
│
├── requirements.txt
├── Dockerfile
├── .env.example
├── README.md
└── .gitignore
```

---

##  Technologies Used

- Python 3.12
- Transformers
- Hugging Face
- Qwen 2.5 0.5B Instruct
- Fireworks AI API
- DeepSeek V4 Pro
- Docker

---

##  Installation

Clone the repository

```bash
git clone https://github.com/raiankur-dev/smart_route_ai.git

cd smart_route_ai
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

##  Environment Variables

Create a `.env` file

```env
FIREWORKS_API_KEY=YOUR_FIREWORKS_API_KEY
```

---

##  Running the Project

Execute

```bash
python src/main.py
```

The generated responses will be stored in

```
output/results.json
```

---

##  Docker

Build the container

```bash
docker build -t smart-route-ai .
```

Run

```bash
docker run --env-file .env smart-route-ai
```

---

##  Example Routing

| Prompt | Routed To |
|---------|-----------|
| What is the capital of France? | Local Qwen |
| Summarize AI in one sentence | Local Qwen |
| Write a Python function to reverse a linked list | DeepSeek |
| Solve x² − 5x + 6 = 0 | DeepSeek |

---

##  Future Improvements

- Fine-tuned routing model instead of rule-based classification
- Confidence-based dynamic routing
- Token cost estimation before inference
- Benchmarking on larger evaluation datasets
- Adaptive routing using response quality feedback

---

##  Team

Developed for the **AMD Developer Hackathon ACT II – Track 1**

Team: *(Add your team name here)*

---

##  License

This project is created solely for the AMD Developer Hackathon ACT II.