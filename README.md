#  Smart Route AI

> **A Hybrid Token-Efficient LLM Routing Agent built for the AMD Developer Hackathon ACT II – Track 1**

Smart Route AI intelligently routes user prompts to either a **local lightweight LLM (Qwen2.5-0.5B-Instruct)** or a **Fireworks-hosted remote LLM** based on task complexity.

Instead of sending every request to a cloud model, Smart Route AI performs lightweight prompt analysis and automatically decides whether the task can be handled locally or requires a more capable remote model. This minimizes API token usage while maintaining high response quality.

---

#  Live Demo

### 🌐 Streamlit

https://smartrouteai-abfp46dmaiemwjnupjht6k.streamlit.app/

---

# 🐳 Docker

### Docker Hub

```
noobmaster732/smart-route-ai
```

Pull the image

```bash
docker pull noobmaster732/smart-route-ai:latest
```

Run

```bash
docker run --env-file .env noobmaster732/smart-route-ai:latest
```

---

# ✨ Features

- 🧠 Hybrid Local + Remote LLM Routing
- ⚡ Complexity-aware prompt analysis
- 💻 Local inference using Qwen2.5-0.5B-Instruct
- ☁️ Remote inference using Fireworks AI
- 💰 Token-efficient architecture
- 🔄 Automatic routing decisions
- 📊 Transparent routing explanation
- 🌐 Interactive Streamlit interface
- 🐳 Dockerized deployment

---

# 🌐 Demo

## Home Page

![Home](images/home.png)

---

## Example 1 – Simple Factual Question

Prompt

```text
What is the capital of France?
```

### Routing Decision

- Task Type: FACTUAL
- Complexity Score: 0
- Selected Model: Local Qwen

![Local Routing](images/local-routing.png)

Simple factual prompts remain on the local model, eliminating unnecessary API usage.

---

## Example 2 – Programming Task

Prompt

```text
Write a Python function to reverse a linked list.
```

### Routing Decision

- Task Type: CODE
- Complexity Score: 4
- Selected Model: Fireworks-hosted LLM

![Remote Routing](images/remote-routing.png)

Programming tasks require stronger reasoning and are therefore routed to the remote model.

---

## Generated Response

![Remote Response](images/remote-response.png)

---

## Generated Output

![Output](images/code-output.png)

---

## Code Preview

![Code Preview](images/code-snippet.png)

---

#  Architecture

```
                     User Prompt
                          │
                          ▼
                 Prompt Classification
                          │
                          ▼
                Complexity Estimation
                          │
                          ▼
                  Intelligent Router
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
     Local Qwen2.5-0.5B         Fireworks AI Hosted LLM
       (CPU Inference)             (Remote Inference)
              │                         │
              └────────────┬────────────┘
                           ▼
                    Final Response
```

---

# ⚙️ Routing Strategy

The routing engine computes a lightweight complexity score using prompt characteristics.

Factors considered include:

- Programming tasks
- Mathematical reasoning
- Logical reasoning
- Prompt length
- Formatting constraints

| Prompt Type | Routed To |
|--------------|-----------|
| Factual Questions | 🟢 Local |
| Summarization | 🟢 Local |
| Named Entity Recognition | 🟢 Local |
| Sentiment Analysis | 🟢 Local |
| Code Generation | 🔴 Remote |
| Mathematical Problems | 🔴 Remote |
| Logical Reasoning | 🔴 Remote |

During hackathon evaluation, the application automatically uses the model(s) provided through the **`ALLOWED_MODELS`** environment variable, ensuring compatibility with the official evaluation harness.

---

# 📁 Project Structure

```
smart_route_ai/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
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
│
├── images/
│   ├── home.png
│   ├── local-routing.png
│   ├── remote-routing.png
│   ├── remote-response.png
│   ├── code-output.png
│   └── code-snippet.png
```

---

# 🛠 Tech Stack

- Python
- Streamlit
- Hugging Face Transformers
- Qwen2.5-0.5B-Instruct
- Fireworks AI
- OpenAI SDK
- Docker
- PyTorch

---

#  Running Locally

Clone the repository

```bash
git clone https://github.com/raiankur-dev/smart_route_ai.git

cd smart_route_ai
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env`

```text
FIREWORKS_API_KEY=YOUR_FIREWORKS_API_KEY

FIREWORKS_BASE_URL=https://api.fireworks.ai/inference/v1

HF_TOKEN=YOUR_HUGGINGFACE_TOKEN
```

Run the Streamlit application

```bash
streamlit run app.py
```

Run the CLI version

```bash
python src/main.py
```

> **Note:** During local development, the application defaults to a Fireworks-hosted model when `ALLOWED_MODELS` is not provided. During hackathon evaluation, the runtime automatically uses the model IDs supplied through the `ALLOWED_MODELS` environment variable.

---

#  Example Routing

| Prompt | Selected Model |
|---------|----------------|
| What is the capital of France? | 🟢 Local |
| Summarize Artificial Intelligence in one sentence. | 🟢 Local |
| Write a Python function to reverse a linked list. | 🔴 Remote |
| Solve x² − 5x + 6 = 0 | 🔴 Remote |

---

#  Key Highlights

- Intelligent Hybrid Routing
- Token-Efficient Inference
- Automatic Local/Remote Model Selection
- Compatible with AMD Evaluation Harness
- Dockerized Deployment
- Public Streamlit Demo
- Public Docker Hub Image
- Explainable Routing Decisions

---

#  Future Improvements

- Machine learning–based routing instead of heuristic rules
- Confidence-aware routing
- Dynamic token cost estimation
- Multi-model remote selection
- Automatic benchmarking
- Adaptive routing based on historical performance

---

#  Team

Developed for the **AMD Developer Hackathon ACT II – Track 1**

**Team:** *<Your Team Name>*

---

#  License

This project was developed as part of the **AMD Developer Hackathon ACT II**.