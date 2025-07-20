
import re
from typing import Optional
from core.prompt_spec import PromptSpec

class Verifier:
    """
    Fügt Prompt-Anweisungen hinzu, die das LLM zur Selbstprüfung seiner Antwort auffordern.
    """

    def wrap_with_verification(self, prompt: str) -> str:
        """
        Ergänzt den Prompt mit einem Verifikationshinweis.
        :param prompt: Der ursprüngliche Prompt
        :return: Erweiterter Prompt mit Verifikationsanweisung
        """
        verification_block = (
            "\n\nBefore responding, verify that your output:\n"
            "- Aligns with the stated intent\n"
            "- Respects all constraints\n"
            "- Fulfills the specified steps\n"
            "- Matches the desired output format (if defined)"
        )
        return prompt + verification_block

    def verify_output(self, response: str, spec: PromptSpec) -> Optional[str]:
        """
        Führt einfache Überprüfung der LLM-Antwort gegen die Constraints und Formatvorgaben durch.
        :param response: Die LLM-Antwort
        :param spec: Das zugrundeliegende PromptSpec-Objekt
        :return: Fehlermeldung oder None, wenn alle Checks bestanden wurden
        """
        # Formatcheck
        if spec.output_format and "```" not in response:
            return f"Fehlendes Code-Format im Output, obwohl '{spec.output_format}' gefordert wurde."

        # Constraint-Check (rein textbasiert)
        for constraint in spec.constraints:
            if constraint.lower() not in response.lower():
                return f"Constraint '{constraint}' nicht erfüllt im Output."

        # Check auf Schritte (sequentielle Keywords)
        for step in spec.step:
            if not any(keyword.lower() in response.lower() for keyword in step.split()):
                return f"Step '{step}' nicht nachvollziehbar im Output."

        return None