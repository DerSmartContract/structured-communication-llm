# prompt_spec.py

from pydantic import BaseModel, Field, validator
from typing import List, Optional


class PromptSpec(BaseModel):
    role: str = Field(..., description="Die Rolle, in der das LLM agieren soll.")
    intent: str = Field(..., description="Das Ziel des Prompts.")
    constraints: Optional[List[str]] = Field(default=[], description="Einschränkungen, die eingehalten werden müssen.")
    context: Optional[List[str]] = Field(default=[], description="Kontextinformationen, die dem LLM zur Verfügung stehen.")
    step: Optional[List[str]] = Field(default=[], description="Schritte, die das LLM durchführen soll.")
    output_format: Optional[str] = Field(default=None, description="Format des erwarteten Outputs.")
    verification_instruction: Optional[str] = Field(default=None, description="Anleitung zur Verifikation des Outputs.")

    @validator("constraints", "context", "step", pre=True)
    def ensure_list(cls, v):
        if isinstance(v, str):
            return [v]
        return v