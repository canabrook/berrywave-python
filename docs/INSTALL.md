# Installing the BerryWave Python EDI SDK

This guide walks through installing the BerryWave Python EDI SDK and preparing a working environment for running the examples and benchmarks.

---

## Prerequisites

The SDK requires:

- Python 3.11 or later
- Java 21 or later

Verify your installation:

```bash
python --version
java --version
```
On some systems, especially macOS and Linux, the system Python command may
be named `python3`.
---

## Download the Release

Download the latest GitHub release assets:

- `berrywave_edi-<version>-py3-none-any.whl`
- `berrywave_edi_examples-<version>.zip`
- `berrywave_edi_benchmarks-<version>.zip`

---

## Create a Working Directory

Create a directory for experimenting with the SDK.

For example:

```text
my-berrywave-test/
```

Change into that directory:

```bash
cd my-berrywave-test
```

---

## Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate it.

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows:

```text
.venv\Scripts\activate
```

Verify the environment:

```bash
python --version
pip --version
```

---

## Install the SDK

Install the downloaded wheel:

```bash
pip install berrywave_edi-<version>-py3-none-any.whl
```

Verify the installation:

```bash
pip show berrywave-edi
```

The SDK is now installed.

---

## Working Directory Layout

Extract the examples and benchmark archives into the same working directory that contains the virtual environment.

A typical layout is:

```text
my-berrywave-test/
│
├── .venv/
│
├── berrywave_edi_examples-<version>/
│
└── berrywave_edi_benchmarks-<version>/
```

Keeping these directories together allows the examples and benchmark programs to locate their accompanying sample data.

---

## Install Optional Benchmark Dependencies

The benchmark programs generate charts using Matplotlib.

Install it if you intend to run the benchmarks:

```bash
pip install matplotlib
```

---

## Verify the Installation

Run one of the example programs:

```bash
cd berrywave_edi_examples-<version>

python -m examples.edi_to_json.850_to_json_pretty
```

If everything is installed correctly, the example will produce normalized JSON output.

---

## Next Steps

See:

- **EXAMPLES.md** — Running the example programs
- **BENCHMARKS.md** — Running the benchmark suite

---

## Troubleshooting

### JPype cannot start the JVM

Verify that Java 21 or later is installed:

```bash
java --version
```

---

### `ModuleNotFoundError`

Ensure the virtual environment is activated before running examples:

macOS/Linux:

```bash
source .venv/bin/activate
```

---

### Benchmark cannot find `benchmark_data`

Run the benchmark from the extracted benchmark directory:

```bash
cd berrywave_edi_benchmarks-<version>

python -m benchmarks.benchmark_claims
```

The benchmark expects the `benchmark_data` directory to be located alongside the `benchmarks` package.

---

### `ModuleNotFoundError: matplotlib`

Install Matplotlib into the active virtual environment:

```bash
pip install matplotlib
```

---

If problems persist, please open an issue on the project's GitHub repository.