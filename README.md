<h1>
  <img src="docs/images/berrywave-logo.png" alt="BerryWave Logo" width="36" height="36" valign="middle">
  BerryWave EDI Python SDK
</h1>

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Java](https://img.shields.io/badge/Java-21%2B-orange)
![License](https://img.shields.io/badge/License-Apache%202.0-green)
![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey)

> **Convert X12 and EDIFACT EDI documents to JSON using a simple, Python-native API.**

The BerryWave EDI Python SDK provides a simple, Python-native interface for working with EDI documents while leveraging the proven BerryWave Software EDI processing engine.

The same EDI engine powers the BerryWave API for EDI, a REST API for EDI processing. The Python SDK provides an alternative integration approach for Python applications, automation workflows, data pipelines, and AI-enabled applications that prefer a native Python interface.

The Python SDK source code is fully available in this repository.

The underlying BerryWave EDI processing engine is developed and maintained by BerryWave Software and is distributed as prebuilt runtime libraries.

---

## Current Release

The initial public release focuses on **core EDI-to-JSON conversion**:

- Convert X12 EDI to JSON
- Convert EDIFACT to JSON
- Optional pretty-printed JSON output
- No BerryWave license required
- **Fully local processing. No network connection or external service required. EDI data never needs to leave the machine**

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

The SDK includes a growing collection of working examples demonstrating common EDI-to-JSON use cases.

Examples cover:

- X12 transaction sets, including healthcare 837 claims and supply-chain 850 purchase orders
- EDIFACT messages
- EDI and JSON using strings or files
- Pretty-printed JSON output
- EDI parsing and error handling

The examples are distributed separately with each GitHub release.

---

## Installation

The recommended way to install the BerryWave EDI Python SDK is from the release assets available on the project's GitHub
Releases page.

Each release includes:

- `berrywave_edi-*.whl` — the Python SDK package
- `berrywave_edi_examples-*.zip` — example programs and sample EDI documents

---

### Install the SDK

Download the latest wheel file:

```text
berrywave_edi-0.1.0-py3-none-any.whl
```

Create and activate a Python virtual environment:

```bash
python -m venv .venv

source .venv/bin/activate
```

Install the SDK:

```bash
pip install berrywave_edi-0.1.0-py3-none-any.whl
```

Verify the installation:

```bash
python -c "import berrywave; print(berrywave)"
```

The SDK is now ready to use.

---

### Run the Examples

Download and extract the examples archive:

```text
berrywave_edi_examples-0.1.0.zip
```

The examples include:

- X12 850 Purchase Order conversion
- X12 837 Healthcare Claim conversion
- EDIFACT ORDERS conversion
- Pretty-printed JSON output
- EDI parsing error handling

After extracting the examples:

```bash
cd berrywave_edi_examples
```

Run an example:

```bash
python -m examples.850_to_json
```

The examples demonstrate the SDK using representative EDI documents and require only the installed BerryWave EDI Python SDK.

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

The Python layer presents a clean, Pythonic interface while the underlying EDI processing remains implemented in the
BerryWave EDI engine. Most applications never need to know that the implementation is written in Java.

---

## Security

The BerryWave EDI engine is designed for environments where EDI data must remain under customer control.

Features include:

- No network connectivity required
- No inbound or outbound network connections
- Suitable for on-premise deployment
- Suitable for air-gapped environments
- Customer-controlled processing of sensitive EDI documents

All EDI processing occurs entirely on the local machine.

---

## Roadmap

Planned enhancements include:

- Additional EDI services
  - JSON to EDI
  - Compliance checking using EDI models
  - Functional acknowledgments
  - Business acknowledgments. For example,  850 → 855 and 837 → 277.
  - JSONata transformation of JSON output
- More ready-to-run benchmarks
- Rich Python exception hierarchy
- Distribution through PyPI


---

## Requirements

- Python 3.11 or later
- Java 21 or later

The BerryWave EDI Python SDK uses a local Java runtime to execute the BerryWave EDI processing engine.


---

## About BerryWave Software

BerryWave Software develops EDI solutions designed to simplify integration between business systems, applications, and trading partners.

The BerryWave API for EDI provides REST-based access to the same BerryWave EDI processing engine used by this Python SDK.

For more information about the REST API approach, see:

https://github.com/RBMayberry/BerryWave-EDI-API

This repository contains the complete BerryWave EDI Python SDK source code.

The BerryWave EDI processing engine is developed and maintained by BerryWave Software and is distributed as prebuilt runtime libraries included with the SDK.


---

## License

The Python source code in this repository is licensed under the project's LICENSE file.

The BerryWave EDI processing engine and associated runtime libraries are licensed separately by BerryWave.