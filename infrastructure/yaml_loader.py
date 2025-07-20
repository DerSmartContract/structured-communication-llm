

import yaml
from pathlib import Path
from core.prompt_spec import PromptSpec


def load_and_validate_yaml(yaml_path: str) -> PromptSpec:
    """
    Lädt eine YAML-Datei und validiert sie gegen das PromptSpec-Modell.
    :param yaml_path: Pfad zur YAML-Datei
    :return: Validiertes PromptSpec-Objekt
    """
    with Path(yaml_path).open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    return PromptSpec(**data)