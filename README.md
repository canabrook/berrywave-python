# BerryWave Python EDI SDK

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Java](https://img.shields.io/badge/Java-21%2B-orange)
![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey)

The **BerryWave Python EDI SDK** is a high-performance SDK for converting X12 and EDIFACT EDI documents to normalized JSON using a simple, Python-native API.

It combines a clean Python interface with the mature BerryWave EDI processing engine, enabling Python applications, automation workflows, AI applications, and data pipelines to process EDI entirely on the local machine.

The same processing engine also powers the BerryWave API for EDI. The Python SDK provides a native Python alternative for applications that prefer an in-process library instead of a REST API.

Additional documentation is provided in focused guides covering installation, examples, and performance benchmarking.

The Python SDK source code is fully available in this repository. The underlying BerryWave EDI processing engine is developed and maintained by BerryWave Software and is distributed as prebuilt runtime libraries.

---

# Features

The current Community Edition supports:

- Convert X12 EDI documents to normalized JSON
- Convert EDIFACT documents to normalized JSON
- Generate X12 997 / 999 acknowledgments
- Generate EDIFACT CONTRL acknowledgments
- String-based and file-based APIs
- Optional pretty-printed JSON output
- Fully local processing
- No network connection required

The SDK is organized around five simple operations:

| Method | Purpose |
|---------|---------|
| `edi_to_json()` | Convert EDI to normalized JSON |
| `json_to_edi()` | Convert normalized JSON back to EDI *(Enterprise Edition)* |
| `acknowledge()` | Generate a technical acknowledgment |
| `validate()` | Validate an EDI document *(Enterprise Edition)* |
| `respond()` | Generate a business response *(Enterprise Edition)* |

---

# Quick Example

```python
from berrywave import EdiService

service = EdiService()

json_document = service.edi_to_json(edi_document)

print(json_document)
```

Generating a technical acknowledgment is equally simple:

```python
ack = service.acknowledge(
    edi_document,
    response_type="999"
)

print(ack)
```

---

# Documentation

The project documentation is organized into focused guides:

| Guide | Description |
|------|-------------|
| [Installation Guide](docs/INSTALL.md) | Installation, virtual environments, verification, and getting started |
| [Examples Guide](docs/EXAMPLES.md) | Complete guide to the included example programs |
| [Benchmarks Guide](docs/BENCHMARKS.md) | Running the claims benchmarks and interpreting performance results |
---

# Architecture

The SDK is intentionally layered.

```text
Python Application
        │
        ▼
BerryWave Python EDI SDK
        │
        ▼
BerryWave EDI Processing Engine
        │
        ▼
X12 / EDIFACT Processing
```

The Python layer presents a clean, Pythonic interface while the underlying EDI processing remains implemented in the BerryWave EDI engine. Most applications never need to know that the implementation is written in Java.

---

# Security

The BerryWave EDI processing engine is designed for environments where EDI data must remain under customer control.

Features include:

- No network connectivity required
- No inbound or outbound network connections
- Suitable for on-premise deployment
- Suitable for air-gapped environments
- Customer-controlled processing of sensitive EDI documents

All EDI processing occurs entirely on the local machine.

---

# Requirements

- Python 3.11 or later
- Java 21 or later

The BerryWave Python EDI SDK uses a local Java runtime to execute the BerryWave EDI processing engine.

---

# About BerryWave Software

BerryWave Software develops EDI solutions designed to simplify integration between business systems, applications, and trading partners.

The BerryWave API for EDI provides REST-based access to the same BerryWave EDI processing engine used by this SDK.

Repository:

https://github.com/RBMayberry/BerryWave-EDI-API

This repository contains the complete BerryWave Python SDK source code.

The BerryWave EDI processing engine and associated runtime libraries are included with the SDK distribution and licensed separately.

---

# License

The Python source code in this repository is licensed under the project's LICENSE file.

The BerryWave EDI processing engine and associated runtime libraries are licensed separately by BerryWave.