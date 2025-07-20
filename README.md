# SCL Framework – Structured Communication Language for LLMs

Das SCL Framework ermöglicht eine präzise, nachvollziehbare und strukturierte Kommunikation mit Large Language Models (LLMs). Es übersetzt YAML-basierte Spezifikationen in validierte Prompts, führt automatische Selbstverifikation durch und reflektiert LLM-Antworten zur kontinuierlichen Verbesserung.

## Features

- ✅ YAML-basierte Prompt-Spezifikationen
- ✅ Validierung mit `pydantic`
- ✅ Automatisierte Prompt-Verifikation
- ✅ Reflexionsmodul zur Ergebnisanalyse
- ✅ CLI und Web-UI (Streamlit)
- ✅ Unterstützung für OpenAI GPT-4o oder lokale Simulation

## Projektstruktur

```bash
scl_framework/
├── agents/                # Prompt-Orchestrierung
├── core/                  # Parser, Validator, Thinker, Verifier, Memory
├── infrastructure/        # LLM-Zugriff, YAML-Lader
├── interface/             # CLI und Web-UI
├── examples/              # Beispiel-Prompts
├── tests/                 # Pytest-Tests
└── README.md              # Dokumentation
```

## Schnellstart

### 1. Virtuelle Umgebung erstellen und aktivieren

**Für macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Für Windows (PowerShell):**

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

### 3. .env konfigurieren

```env
OPENAI_API_KEY=sk-...
```

### 4. Ausführen über CLI

```bash
python interface/cli.py examples/real_estate_ux.yaml --use-openai
```

Oder ohne OpenAI (lokale Simulation):

```bash
python interface/cli.py examples/real_estate_ux.yaml

python -m interface.cli examples/real_estate_ux.yaml
```

### 5. Ausführen über Web-UI

```bash
streamlit run interface/web_ui.py
```

## Beispielprompt

Datei: `examples/real_estate_ux.yaml`

```yaml
role: "UX-Architect"
intent: "Verbessere die Benutzerführung auf einer Immobilien-Website für Senioren"
constraints:
  - "Nutzung altersfreundlicher Sprache"
  - "Minimale Klicktiefe (max. 3 Klicks)"
  - "Barrierefrei laut WCAG 2.1"
context:
  - "Zielgruppe: Senioren 65+"
  - "Problem: aktuelle Seite ist zu textlastig und unübersichtlich"
step:
  - "Analysiere das aktuelle Design"
  - "Stelle 3 Prinzipien guter UX für Senioren auf"
  - "Entwerfe 2 grobe UI-Layouts"
output_format: "markdown mit Codeblöcken"
verification_instruction: "Erkläre, wie jede Designentscheidung auf das Ziel einzahlt"
```

## Testen

```bash
pytest tests/
```
