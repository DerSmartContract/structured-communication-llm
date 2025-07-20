#memory.py

class Memory:
    """
    Einfaches deklaratives Gedächtnismodul für Prompt-Iterationen.
    Speichert Schlüssel-Wert-Paare und ermöglicht selektiven Abruf.
    """

    def __init__(self):
        self.entries = []

    def add(self, key: str, value: str):
        """
        Speichert einen neuen Eintrag im Gedächtnis.
        :param key: Thematischer Schlüssel
        :param value: Inhalt oder LLM-Antwort
        """
        self.entries.append((key, value))

    def recall(self, key: str) -> list[str]:
        """
        Ruft alle Einträge zu einem Schlüssel ab.
        :param key: Der gesuchte Schlüssel
        :return: Liste mit allen passenden Werten
        """
        return [v for k, v in self.entries if k == key]

    def last(self) -> str:
        """
        Gibt den zuletzt gespeicherten Wert zurück (unabhängig vom Schlüssel).
        :return: Letzter gespeicherter Wert oder Hinweis
        """
        if not self.entries:
            return "Memory is empty."
        return self.entries[-1][1]