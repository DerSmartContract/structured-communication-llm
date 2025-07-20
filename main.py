import sys
import os
import argparse
import subprocess

def run_cli(yaml_path, use_openai=False):
    args = ["python", "-m", "interface.cli", yaml_path]
    if use_openai:
        args.append("--use-openai")
    subprocess.run(args)

def run_web():
    #subprocess.run(["streamlit", "run", "interface/web_ui.py"])
    env = os.environ.copy()
    env["PYTHONPATH"] = os.getcwd()
    subprocess.run(["streamlit", "run", "interface/web_ui.py"], env=env)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SCL Framework Hauptmodul")
    parser.add_argument("--cli", type=str, help="Pfad zur YAML-Datei für CLI-Modus")
    parser.add_argument("--use-openai", action="store_true", help="GPT-4o aktivieren")
    parser.add_argument("--web", action="store_true", help="WebUI starten")
    args = parser.parse_args()

    if args.cli:
        run_cli(args.cli, use_openai=args.use_openai)
    elif args.web:
        run_web()
    else:
        print("⚠️ Bitte --cli <yaml> oder --web angeben.")