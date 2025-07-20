# thinker.py
from typing import List


class Thinker:
    """
    Das Thinker-Modul reflektiert über die LLM-Antworten und liefert Feedback für Iterationen.
    """

    def reflect(self, history: list[str]) -> str:
        """
        Analysiert die letzte Antwort im Verlauf und formuliert eine Reflexionsfrage oder Verbesserungsvorschlag.
        :param history: Liste früherer LLM-Antworten.
        :return: Reflexionsvorschlag für den nächsten Prompt-Durchlauf.
        """
        if not history:
            return "Keine vorherige Antwort zur Reflexion verfügbar."
        last = history[-1]
        return (
            "Reflektiere über die letzte Antwort:\n"
            f"{last}\n\n"
            "Gibt es Verbesserungspotenzial hinsichtlich Zielerreichung, Klarheit oder Struktur?"
        )