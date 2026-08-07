# BerryWave Python EDI SDK Benchmarks

The BerryWave Python EDI SDK includes a benchmark suite for measuring EDI-to-JSON conversion performance using synthetic X12 837 Professional Healthcare Claim (837P) documents.

The benchmarks are intended to evaluate throughput on your own hardware using datasets ranging from small test files to very large production-scale documents.

---

## Prerequisites

Before running the benchmarks:

- Install the BerryWave Python EDI SDK (see **INSTALL.md**)
- Install Matplotlib:

```bash
pip install matplotlib
```

---

## Benchmark Package

Extract the benchmark archive into the same working directory used during installation.

The extracted directory contains:

```text
berrywave_edi_benchmarks-<version>/
│
├── benchmarks/
│   ├── benchmark_claims.py
│   ├── benchmark_scaling.py
│   └── benchmark_file_conversion.py
│
└── benchmark_data/
```

The benchmark programs automatically locate the `benchmark_data` directory.

---

## Running the Claims Benchmark

Change into the benchmark directory:

```bash
cd berrywave_edi_benchmarks-<version>
```

Run the benchmark:

```bash
python -m benchmarks.benchmark_claims
```

---

## Benchmark Dataset

The benchmark suite includes synthetic X12 837 Professional Healthcare Claim documents of increasing size.

The benchmark files follow the naming convention:

```text
837-<transactions>-<claims>.edi
```

where:

- `<transactions>` is the number of `ST` transaction sets in the file.
- `<claims>` is the number of healthcare claims contained in each transaction.

The total number of claims is therefore:

```text
transactions × claims
```

Example:

| File | Transactions | Claims per Transaction | Total Claims |
|------|-------------:|-----------------------:|-------------:|
| `837-100-100.edi` | 100 | 100 | 10,000 |
| `837-1000-100.edi` | 1,000 | 100 | 100,000 |
| `837-1000-1000.edi` | 1,000 | 1,000 | 1,000,000 |

The largest benchmark document contains **one million healthcare claims**.

---

## What the Benchmark Measures

For each benchmark file, the program:

- Converts the EDI document to normalized JSON using the SDK's file-to-file API
- Measures total conversion time
- Calculates claims processed per second
- Reports input file size
- Reports output file size
- Reports the total number of claims processed

---

## Benchmark Results

After processing all benchmark files, the benchmark generates:

- A summary table
- A CSV file containing the benchmark results
- A scatterplot showing throughput (claims per second) as a function of total claims processed

The CSV output can be imported into spreadsheet or reporting tools for additional analysis.

---

## Expected Runtime

The complete benchmark suite typically requires approximately **3–5 minutes**, depending on your hardware.

The benchmark processes the largest dataset containing **1,000,000 healthcare claims**, so the runtime is intentionally long enough to provide meaningful throughput measurements.

---

## Benchmark Data

All benchmark documents are **synthetically generated** specifically for performance testing.

They contain realistic X12 837 structures while using entirely fictitious:

- patient names
- provider names
- addresses
- identifiers
- payer information

No real healthcare data is included.

---

## Running Individual Benchmarks

You may remove benchmark files that you do not wish to execute.

The benchmark automatically discovers every file in the `benchmark_data` directory matching:

```text
837-*.edi
```

Only the files present in the directory will be processed.

This makes it easy to benchmark small, medium, or very large datasets independently.

---

## Comparing Systems

Because the benchmark executes entirely on the local machine, it provides a convenient way to compare:

- different processors
- memory configurations
- operating systems
- Python versions
- Java runtime versions

using the same benchmark data and benchmark program.

---

## Troubleshooting

### `ModuleNotFoundError: matplotlib`

Install Matplotlib:

```bash
pip install matplotlib
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

### Benchmark appears slow

The largest benchmark processes **one million healthcare claims**.

Depending on your system, the complete benchmark suite typically requires **3–5 minutes** to complete.

This is expected.