

import os
import openai
from typing import Callable


class LLMWrapper:
    """
    Universelle LLM-Schnittstelle mit Unterstützung für GPT-4o via OpenAI oder lokale Simulation.
    """

    def __init__(self, use_openai: bool = False, model: str = "gpt-4o"):
        """
        Initialisiert das LLM-Modul.
        :param use_openai: True = OpenAI API, False = lokal/dummy
        :param model: Modellbezeichnung bei OpenAI
        """
        self.use_openai = use_openai
        self.model = model
        self.api_key = os.getenv("OPENAI_API_KEY", "")

        if self.use_openai and not self.api_key:
            raise ValueError("OPENAI_API_KEY ist nicht gesetzt.")

        if self.use_openai:
            openai.api_key = self.api_key

    def __call__(self, prompt: str) -> str:
        if self.use_openai:
            return self._call_openai(prompt)
        return self._call_local(prompt)

    def _call_local(self, prompt: str) -> str:
        return f"[SIMULIERTE LLM-ANTWORT]\n\n{prompt}"

    def _call_openai(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
        )
        return response.choices[0].message["content"].strip()