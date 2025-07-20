

import streamlit as st
from agents.scl_agent import SCLAgent
from infrastructure.yaml_loader import load_and_validate_yaml
from openai import OpenAI



def simple_llm(prompt: str) -> str:
    # Dummy-LLM zur Demonstration
    return f"[LLM-Output simuliert]\n\n{prompt}"


st.set_page_config(page_title="SCL Framework UI", layout="wide")

st.title("🧠 SCL Framework – Strukturierte Kommunikation mit LLMs")

uploaded_file = st.file_uploader("Lade eine YAML-Spezifikation hoch", type=["yaml", "yml"])

if uploaded_file is not None:
    yaml_bytes = uploaded_file.read()
    yaml_text = yaml_bytes.decode("utf-8")

    with open("temp_uploaded.yaml", "w", encoding="utf-8") as f:
        f.write(yaml_text)

    st.code(yaml_text, language="yaml")

    agent = SCLAgent(llm=simple_llm)

    with st.spinner("LLM wird ausgeführt..."):
        try:
            result, reflection = agent.run("temp_uploaded.yaml")
            st.subheader("📄 Ergebnis:")
            st.text(result)
            st.subheader("🔁 Reflexion:")
            st.text(reflection)
        except Exception as e:
            st.error(f"Fehler: {e}")