import streamlit as st
import sys
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.append(str(ROOT / "src"))

from router import route, route_prompt

st.set_page_config(
    page_title="Smart Route AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🧠 Smart Route AI")
st.caption("Hybrid LLM Router • Local Qwen + Remote DeepSeek • Token Efficient Inference")

prompt = st.text_area(
    "Enter your prompt",
    height=180,
    placeholder="Ask anything..."
)

if st.button("🚀 Generate Response", use_container_width=True):

    if prompt.strip():

        with st.spinner("Routing prompt..."):

            # Get routing decision
            decision = route_prompt(prompt)

            # Generate answer
            answer = route(prompt)

        st.success("Response Generated!")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Task Type", decision["task"])

        with col2:
            st.metric(
                "Complexity Score",
                f"{decision['complexity']}/10"
            )

        with col3:
            if decision["model"] == "LOCAL":
                st.metric("Chosen Model", "🟢 Local Qwen")
            else:
                model_name = decision["remote_model"].split("/")[-1]
                st.metric("Chosen Model", f"🔴 {model_name}")

        st.markdown("---")

        st.subheader("Why this route?")

        for reason in decision["reason"]:
            st.write(f"✅ {reason}")

        st.markdown("---")

        st.subheader("Response")

        st.write(answer)

    else:
        st.warning("Please enter a prompt.")