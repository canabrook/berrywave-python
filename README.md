<h1>
  <img src="docs/images/berrywave-logo.png" alt="BerryWave Logo" width="36" height="36" valign="middle">
  BerryWave Python EDI SDK
</h1>

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Java](https://img.shields.io/badge/Java-21%2B-orange)
![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey)

The **BerryWave Python EDI SDK** is a high-performance SDK for converting X12 and EDIFACT EDI documents
to normalized JSON using a simple, Python-native API. It combines a clean Python interface
with the mature BerryWave EDI processing engine,
enabling Python applications, automation workflows, data pipelines, and AI-enabled applications and workflows to process EDI entirely on the local machine.

The same EDI processing engine powers the BerryWave API for EDI, a REST API for EDI processing.
The Python SDK provides an alternative integration approach for applications that prefer a native Python interface.

The Python SDK source code is fully available in this repository.
The underlying BerryWave EDI processing engine is developed and maintained by BerryWave Software and is distributed as prebuilt runtime libraries.

The Python SDK source code is fully available in this repository.
The underlying BerryWave EDI processing engine is developed and maintained by BerryWave Software and is distributed as prebuilt runtime libraries.

## Contents

- [Features](#features)
- [Quick Example](#quick-example)
- [Example Programs](#example-programs)
- [Installation and Getting Started](#installation-and-getting-started)
  - [Run the Examples](#run-the-examples)
  - [Run the Claims Benchmarks](#run-the-claims-benchmarks)
- [Architecture](#architecture)
- [Security](#security)
- [Requirements](#requirements)
- [Roadmap](#roadmap)
- [About BerryWave Software](#about-berrywave-software)
- [License](#license)

---

## Features

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

## Installation and Getting Started

The recommended way to install the BerryWave Python EDI SDK is from the release assets available on the project's GitHub Releases page.

Each release includes:

- `berrywave_edi-*.whl` — the Python SDK package
- `berrywave_edi_examples-*.zip` — example programs and sample EDI documents
- `berrywave_edi_benchmarks-*.zip` — benchmark programs and benchmark data

Download the latest wheel file:

    berrywave_edi-0.1.0-py3-none-any.whl

Create and activate a Python virtual environment:

    python -m venv .venv
    source .venv/bin/activate

Confirm that the virtual environment is active:

    python --version
    pip --version

Install and verify the SDK:

    pip install berrywave_edi-0.1.0-py3-none-any.whl
    pip show berrywave-edi

The SDK is now ready to use.

### Run the Examples

Extract the examples archive into its own directory:

    berrywave_edi_examples-0.1.0/

Run examples from that directory:

    cd berrywave_edi_examples-0.1.0
    python -m examples.850_to_json_pretty

The examples demonstrate the SDK using representative EDI documents and require only the installed BerryWave Python EDI SDK.

### Run the Claims Benchmarks

The benchmark package includes a collection of synthetic X12 837 Professional Healthcare Claim (837P) documents of increasing size, ranging from **10,000 claims to 1,000,000 claims**.

To keep the Git repository compact, the benchmark datasets are distributed in the **`berrywave_edi_benchmarks-*.zip`** release asset rather than being stored directly in the repository.

After installing the SDK wheel, extract the benchmark archive into its own directory.

The extracted benchmark directory contains both the benchmark programs and the benchmark data:

    berrywave_edi_benchmarks-0.1.0/
        benchmarks/
        benchmark_data/

Run the benchmark from the extracted benchmark directory:

    cd berrywave_edi_benchmarks-0.1.0
    python -m benchmarks.benchmark_claims

The benchmark automatically discovers all benchmark files in the `benchmark_data` directory whose names follow the pattern:

```text
837-<transactions>-<claims>.edi
```

where:

- `<transactions>` is the number of `ST` transaction sets in the file.
- `<claims>` is the number of claims contained in each transaction.

The total number of claims processed is therefore:

```text
transactions × claims
```

For each benchmark file, the program:

- Converts the EDI document to JSON using the SDK's file-to-file API
- Measures conversion time
- Calculates claims processed per second
- Reports the input and output file sizes
- Reports the total number of claims processed

After all benchmark files have been processed, the benchmark generates:

- A summary table showing:
  - Input file
  - Input size
  - Output size
  - Total claims
  - Conversion time
  - Claims processed per second
- A CSV file containing the benchmark results
- A scatterplot showing throughput (claims per second) as a function of the total number of claims

Depending on your hardware, processing the full benchmark suite—including the 1,000,000-claim dataset—typically requires approximately **3–5 minutes**.
The benchmark runs on your own hardware so that performance can be evaluated and compared under real-world conditions.

The benchmark data consists entirely of synthetically generated healthcare claims created specifically for performance testing. The files contain realistic X12 837 structures while using fictitious names, identifiers, addresses, and payer information suitable for public distribution.


---

## Architecture

The SDK is intentionally layered.

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

The Python layer presents a clean, Pythonic interface while the underlying EDI processing remains implemented in the BerryWave EDI engine.
Most applications never need to know that the implementation is written in Java.

---

## Security

The BerryWave EDI processing engine is designed for environments where EDI data must remain under customer control.

Features include:

- No network connectivity required for EDI processing
- No inbound or outbound network connections
- Suitable for on-premise deployment
- Suitable for air-gapped environments
- Customer-controlled processing of sensitive EDI documents

All EDI processing occurs entirely on the local machine.

---

## Requirements

- Python 3.11 or later
- Java 21 or later

The BerryWave EDI Python SDK uses a local Java runtime to execute the EDI processing engine.

---

## Roadmap

The underlying EDI engine natively supports additional capabilities that will be exposed in future Python SDK releases:

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

This repository contains the complete BerryWave Python EDI SDK source code.

The BerryWave EDI processing engine and associated runtime libraries are included with the SDK distribution and licensed separately.

---

## License

The Python source code in this repository is licensed under the project's LICENSE file.

The BerryWave EDI processing engine and associated runtime libraries are licensed separately by BerryWave.