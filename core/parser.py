#parser.py

from core.prompt_spec import PromptSpec


def parse_scl_prompt(spec: PromptSpec) -> str:
    """
    Erstellt aus einem PromptSpec-Objekt einen vollständigen Prompt-String für das LLM.
    :param spec: Validiertes PromptSpec-Objekt
    :return: Prompt-String
    """
    prompt = f"You are a {spec.role}\n"
    prompt += f"Goal: {spec.intent}\n\n"

    if spec.constraints:
        for c in spec.constraints:
            prompt += f"- Constraint: {c}\n"

    if spec.context:
        for ctx in spec.context:
            prompt += f"- Context: {ctx}\n"

    if spec.step:
        prompt += "\nSteps to follow:\n"
        for idx, step in enumerate(spec.step, 1):
            prompt += f"  {idx}. {step}\n"

    if spec.output_format:
        prompt += f"\nOutput format: {spec.output_format}\n"

    if spec.verification_instruction:
        prompt += f"\nVerify your result by: {spec.verification_instruction}\n"

    return prompt