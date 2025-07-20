# import sys
# from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parent.parent))

import argparse
from agents.scl_agent import SCLAgent
from infrastructure.llm_wrapper import LLMWrapper


def main():
    parser = argparse.ArgumentParser(description="SCL Framework CLI")
    parser.add_argument("yaml_path", type=str, help="Pfad zur YAML-Datei mit Prompt-Spezifikation")
    parser.add_argument("--use-openai", action="store_true", help="Verwende OpenAI GPT-4o statt lokaler Simulation")
    args = parser.parse_args()

    llm = LLMWrapper(use_openai=args.use_openai)
    agent = SCLAgent(llm=llm)

    response, reflection = agent.run(args.yaml_path)

    print("\n--- LLM Response ---\n")
    print(response)
    print("\n--- Reflection ---\n")
    print(reflection)


if __name__ == "__main__":
    main()