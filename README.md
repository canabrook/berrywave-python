# BerryWave EDI Python SDK

A Python interface for the BerryWave EDI processing engine.

The BerryWave EDI Python SDK allows Python applications, automation workflows, data pipelines,
and AI-enabled applications to process EDI transactions using a simple Python API while leveraging the BerryWave EDI engine.

The Python SDK source code is available in this repository.
The underlying BerryWave EDI processing engine remains proprietary software owned by BerryWave.

---

## Overview

EDI processing is often embedded in enterprise systems, but modern workflows increasingly involve:

- Python automation
- data analysis
- machine learning and AI workflows
- integration pipelines
- notebooks and developer tools

The BerryWave EDI Python SDK provides a Python-native interface to EDI capabilities without requiring applications to understand the underlying Java implementation.

Example:

    from berrywave import EdiService

    edi_service = EdiService()

    json_text = edi_service.edi_to_json(edi_document)

    print(json_text)

---

## Features

Current capabilities include:

- EDI to JSON conversion
- JSON to EDI conversion
- EDI validation
- EDI splitting
- EDI model awareness
- X12 envelope processing
- Python API over the BerryWave EDI engine

Additional services will be added as the SDK evolves.

---

## Architecture

The SDK uses a layered architecture:

    Python Application
            |
            v
    BerryWave Python SDK
            |
            v
    JPype JVM Integration
            |
            v
    BerryWave EDI Engine
            |
            v
    X12 / EDI Processing

The Python layer provides a clean Python interface while the core EDI processing logic remains implemented in the BerryWave engine.

The engine is designed to operate without requiring a Spring-based application environment,
making it suitable for:

- Python applications
- command-line tools
- automation workflows
- AI and data processing environments
- secure on-premise deployments

---

## Security and Deployment Model

The BerryWave EDI engine is designed for environments where EDI data must remain under customer control.

The SDK supports:

- local execution
- no network connections
- on-premise deployment
- customer-controlled data processing

License validation is performed locally by the BerryWave engine.

---

## Installation

Installation instructions will evolve as the package is prepared for distribution.

For development:

    git clone https://github.com/BerryWave/Python-EDI.git

    cd Python-EDI

    python -m venv .venv

    source .venv/bin/activate

    pip install -e .

---

## Quick Example

    from berrywave import EdiService

    service = EdiService()

    edi = """
    ISA...
    GS...
    ST...
    SE...
    GE...
    IEA...
    """

    json_text = service.edi_to_json(edi)

    print(json_text)

---

## Project Structure

    Python-EDI/

    ├── berrywave/
    │   ├── __init__.py
    │   ├── edi_service.py
    │   ├── jvm.py
    │   └── runtime/
    │       └── java/
    │           └── BerryWave engine libraries
    │
    ├── examples/
    │   └── edi_to_json.py
    │
    ├── tests/
    │
    ├── notes/
    │
    ├── pyproject.toml
    └── README.md

---

## Development

Run tests:

    pytest

Run an example:

    python -m examples.edi_to_json

---

## Relationship to BerryWave Products

The Python SDK is an integration layer for the BerryWave EDI processing engine.

The repository contains the Python source code required to interact with the engine. The BerryWave EDI engine itself is proprietary software distributed separately by BerryWave.

---

## Roadmap

Potential future enhancements:

- Additional EDI transaction support
- Improved Python documentation
- Package distribution through PyPI or private package repositories
- Async integration patterns
- AI-assisted EDI workflows
- Additional examples and integrations

---

## License

The Python source code in this repository is licensed under [LICENSE].

The BerryWave EDI engine and associated proprietary components are licensed separately by BerryWave.