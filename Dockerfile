FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip

# Install CPU-only PyTorch
RUN python -m pip install --no-cache-dir \
    --index-url https://download.pytorch.org/whl/cpu \
    torch==2.4.1

# Install everything else explicitly
RUN python -m pip install --no-cache-dir \
    transformers==5.13.0 \
    accelerate==1.14.0 \
    huggingface_hub==1.23.0 \
    python-dotenv==1.2.2 \
    openai==2.45.0 \
    streamlit==1.47.1 \
    sentencepiece==0.2.1 \
    safetensors==0.8.0

COPY . .

RUN mkdir -p output

CMD ["python", "src/main.py"]