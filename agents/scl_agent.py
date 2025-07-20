from core.parser import parse_scl_prompt
from core.verifier import Verifier
from core.thinker import Thinker
from infrastructure.yaml_loader import load_and_validate_yaml


class SCLAgent:
    """
    Der SCLAgent orchestriert die strukturierte Kommunikation zwischen YAML-Spezifikationen
    und einem LLM-Modell. Er übernimmt Parsing, Verifikation, LLM-Kommunikation und Reflexion.
    """

    def __init__(self, llm):
        """
        Initialisiert den Agenten mit einem LLM, Verifikator und Thinker-Modul.
        :param llm: Eine Callable, die einen Prompt-String entgegen nimmt und eine Antwort zurückgibt.
        """
        self.llm = llm
        self.verifier = Verifier()
        self.thinker = Thinker()

    def run(self, yaml_path: str) -> tuple[str, str]:
        """
        Führt eine vollständige LLM-Kommunikation basierend auf einer YAML-Spezifikation durch.
        :param yaml_path: Pfad zur YAML-Datei mit SCL-Struktur.
        :return: Tuple aus LLM-Antwort und Reflexions-Output.
        """
        yaml_data = load_and_validate_yaml(yaml_path)
        base_prompt = parse_scl_prompt(yaml_data)
        verified_prompt = self.verifier.wrap_with_verification(base_prompt)
        response = self.llm(verified_prompt)
        reflection = self.thinker.reflect([response])
        return response, reflection