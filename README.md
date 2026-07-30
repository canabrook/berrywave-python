<h1>
  <img src="docs/images/berrywave-logo.png" alt="BerryWave Logo" width="36" height="36" valign="middle">
  BerryWave EDI Python SDK
</h1>

![Python](https://img.shields.io/badge/Python-3.14%2B-blue)
![Java](https://img.shields.io/badge/Java-21%2B-orange)
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

    from berrywave import EdiService

    service = EdiService()
    json_document = service.edi_to_json(edi_document)
    print(json_document)

---

## Example Programs

The SDK includes a growing collection of working examples demonstrating common EDI-to-JSON use cases.

Examples cover:

- X12 transaction sets, including healthcare 837 claims and supply-chain 850 purchase orders
- EDIFACT messages
- EDI → JSON using string or file input and string or file output
- Pretty-printed JSON output
- EDI parsing and error handling

The examples are distributed separately with each GitHub release.

---

## Installation

The recommended way to install the BerryWave EDI Python SDK is from the release assets available on the project's GitHub Releases page.

Each release includes:

- `berrywave_edi-*.whl` — the Python SDK package
- `berrywave_edi_examples-*.zip` — example programs and sample EDI documents
- `berrywave_edi_benchmarks-*.zip` — benchmark programs and benchmark data

Download the latest wheel file:

    berrywave_edi-0.1.0-py3-none-any.whl

Create and activate a Python virtual environment:

    python -m venv .venv
    source .venv/bin/activate

Install and verify the SDK:

    pip install berrywave_edi-0.1.0-py3-none-any.whl
    pip show berrywave-edi

The SDK is now ready to use.

### Run the Examples

Download and extract the examples archive:

    berrywave_edi_examples-0.1.0.zip

The examples archive contains working examples and representative EDI documents covering the capabilities described above.

After extracting the examples:

    cd berrywave_edi_examples-0.1.0

Run an example:

    python -m examples.850_to_json_pretty

The examples demonstrate the SDK using representative EDI documents and require only the installed BerryWave EDI Python SDK.

### Run the Claims Benchmark

Download and extract the benchmark archive:

    berrywave_edi_benchmarks-0.1.0.zip

After extracting the benchmark archive:

    cd berrywave_edi_benchmarks-0.1.0

Run the healthcare claims benchmark:

    python -m benchmarks.benchmark_claims

The benchmark reports:

- Python version
- Java version
- BerryWave SDK version
- Input and output file sizes
- Number of claims processed
- JVM startup time
- EDI → JSON conversion time
- Conversion throughput
- Claims processed per second

The benchmark is intended to be run on your own machine
so that performance results can be evaluated and compared under real-world conditions.
The provided sample has 10,000 claims, and you are encouraged to benchmark with your own arbitrarily large EDI files.

---

## Architecture

The SDK is intentionally layered.

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

The Python layer presents a clean, Pythonic interface while the underlying EDI processing remains implemented in the BerryWave EDI engine. Most applications never need to know that the implementation is written in Java.

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

## Requirements

- Python 3.14 or later
- Java 21 or later

The BerryWave EDI Python SDK uses a local Java runtime to execute the BerryWave EDI processing engine.

---

## Roadmap

The underlying BerryWave EDI engine natively supports additional capabilities that will be exposed in future Python SDK releases:

* **Engine Capabilities (Coming to Python SDK):**
  * JSON → EDI conversion
  * Compliance checking using EDI models
  * Functional acknowledgments (e.g., 997, 999, CONTRL)
  * Business acknowledgments (e.g., 850 → 855, 837 → 277)
  * JSONata transformation of JSON output
  * Additional EDI standards (e.g., HL7, TRADACOMS)

* **SDK & Packaging Improvements:**
  * Distribution through PyPI
  * Additional ready-to-run benchmarks

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