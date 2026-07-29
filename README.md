# BerryWave EDI Python SDK

A Python SDK for converting EDI documents into structured JSON.

The BerryWave EDI Python SDK provides a simple, Python-native interface for working with EDI documents while leveraging the proven BerryWave EDI processing engine. It is designed for Python applications, automation workflows, data pipelines, and AI-enabled applications that need reliable EDI processing without requiring a REST API.

The Python SDK source code is fully available in this repository.

The underlying BerryWave EDI processing engine is developed and maintained by BerryWave and is distributed as prebuilt runtime libraries.

---

## Current Release

The initial public release focuses on one thing:

- Convert X12 EDI to JSON
- Convert EDIFACT to JSON
- Optional pretty-printed JSON output
- No license required
- Local execution with no network connectivity

Additional EDI services will be added in future releases.

---

## Quick Example

```python
from berrywave import EdiService

service = EdiService()

json_document = service.edi_to_json(edi_document)

print(json_document)
```

---

## Example Programs

The SDK includes working examples demonstrating common use cases:

| Example | Description |
|----------|-------------|
| `850_to_json.py` | Convert an X12 850 Purchase Order to JSON |
| `850_to_json_pretty.py` | Produce indented, human-readable JSON |
| `837_to_json.py` | Convert an X12 837 Healthcare Claim to JSON |
| `edifact_orders_to_json.py` | Convert an EDIFACT ORDERS message to JSON |
| `edi_parse_error.py` | Demonstrate handling EDI parsing exceptions |

Additional examples will be added as the SDK evolves.

---

## Installation

Clone the repository and create a virtual environment.

```bash
git clone https://github.com/BerryWave/Python-EDI.git

cd Python-EDI

python -m venv .venv

source .venv/bin/activate

pip install -e .
```

---

## Architecture

The SDK is intentionally layered.

```
Python Application
        │
        ▼
BerryWave Python SDK
        │
        ▼
BerryWave EDI Engine
        │
        ▼
X12 / EDIFACT Processing
```

The Python layer presents a clean, Pythonic interface while the underlying EDI processing remains implemented in the BerryWave engine.

Most applications never need to know that the implementation is written in Java.

---

## Security

The BerryWave EDI engine is designed for environments where EDI data must remain under customer control.

Features include:

- Local execution
- No outbound network connections
- Suitable for on-premise deployment
- Suitable for air-gapped environments
- Customer-controlled processing of sensitive EDI documents

All EDI processing occurs locally.

---

## Project Structure

```
Python-EDI/

├── berrywave/
│   ├── __init__.py
│   ├── edi_service.py
│   ├── exceptions.py
│   ├── jvm.py
│   └── runtime/
│       └── java/
│
├── examples/
│   ├── 850_to_json.py
│   ├── 850_to_json_pretty.py
│   ├── 837_to_json.py
│   ├── edifact_orders_to_json.py
│   └── edi_parse_error.py
│
├── tests/
│
├── pyproject.toml
│
└── README.md
```

---

## Development

Run the test suite:

```bash
pytest
```

Run an example:

```bash
python -m examples.850_to_json
```

---

## Roadmap

Planned enhancements include:

- Additional EDI-to-JSON examples
- File-based input and output
- Additional EDI services
- Rich Python exception hierarchy
- Improved documentation
- Distribution through PyPI
- Additional AI integration examples

---

## Relationship to BerryWave

This repository contains the complete Python SDK source code.

The BerryWave EDI processing engine is developed and maintained by BerryWave and is distributed as prebuilt runtime libraries included with the SDK.

The goal of this project is to provide a natural, Python-first interface to the BerryWave EDI engine while keeping installation and use as simple as possible.

---

## License

The Python source code in this repository is licensed under the project's LICENSE file.

The BerryWave EDI processing engine and associated runtime libraries are licensed separately by BerryWave.