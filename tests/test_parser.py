


import pytest
from core.prompt_spec import PromptSpec
from core.parser import parse_scl_prompt


def test_parse_scl_prompt_basic():
    spec = PromptSpec(
        role="Research Analyst",
        intent="Analysiere die Auswirkungen von KI auf den Arbeitsmarkt",
        constraints=["keine politischen Aussagen", "max. 500 Wörter"],
        context=["Bericht für die OECD", "Publikumsziel: Entscheidungsträger"],
        step=["Fasse aktuelle Studien zusammen", "Stelle 3 Szenarien dar"],
        output_format="Fließtext mit Bullet Points",
        verification_instruction="Erkläre, wie jede Aussage belegt ist"
    )

    prompt = parse_scl_prompt(spec)
    assert "Research Analyst" in prompt
    assert "Analysiere die Auswirkungen von KI auf den Arbeitsmarkt" in prompt
    assert "- Constraint: keine politischen Aussagen" in prompt
    assert "Steps to follow" in prompt
    assert "Output format: Fließtext mit Bullet Points" in prompt
    assert "Verify your result by" in prompt