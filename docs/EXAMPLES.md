# BerryWave Python EDI SDK Examples

The BerryWave Python EDI SDK includes a growing collection of runnable examples demonstrating the SDK's capabilities.

The examples are distributed separately from the Python package in the release asset:

```text
berrywave_edi_examples-<version>.zip
```

After extracting the archive, the directory structure is:

```text
berrywave_edi_examples-<version>/
│
├── examples/
    ├── edi_to_json/
    ├── acknowledge/
    ├── validate/
    ├── respond/
    ├── json_to_edi/
    └── sdk/
```

Each example is a complete, runnable Python program.

---

# Running an Example

Change into the examples directory:

```bash
cd berrywave_edi_examples-<version>
```

Run an example using Python's module syntax:

```bash
python -m examples.edi_to_json.850_to_json
```

---

# Example Categories

The examples are organized by the SDK's five primary operations.

| Directory | Purpose |
|-----------|---------|
| `edi_to_json/` | Convert EDI documents to normalized JSON |
| `acknowledge/` | Generate technical acknowledgments (997, 999, CONTRL) |
| `validate/` | Validate EDI documents (Enterprise Edition) |
| `respond/` | Generate business responses (855, 277, etc.) |
| `json_to_edi/` | Convert normalized JSON back to EDI (Enterprise Edition) |
| `sdk/` | General SDK information and utilities |

---

# edi_to_json Examples

These examples demonstrate converting EDI documents into normalized JSON.

Current examples include:

| Example | Description |
|---------|-------------|
| `850_to_json.py` | Convert an X12 850 Purchase Order to JSON |
| `850_to_json_pretty.py` | Pretty-print the JSON output |
| `850_to_json_file.py` | File-to-file conversion |
| `837_to_json.py` | Convert an X12 837 Healthcare Claim |
| `837_to_json_pretty.py` | Pretty-print an 837 conversion |
| `edifact_orders_to_json.py` | Convert an EDIFACT ORDERS message |
| `edi_parse_error.py` | Demonstrate parse error handling |

Example:

```bash
python -m examples.edi_to_json.837_to_json
```

---

# acknowledge Examples

Technical acknowledgments verify that an EDI document was successfully received and parsed.

Examples currently include:

| Example | Description |
|---------|-------------|
| `acknowledge_850.py` | Generate a 997 or 999 for an X12 850 |
| `acknowledge_837.py` | Generate a 997 or 999 for an X12 837 |
| `acknowledge_ORDERS.py` | Generate a CONTRL message for an EDIFACT ORDERS document |

Example:

```bash
python -m examples.acknowledge.acknowledge_850
```

---

# validate Examples

Validation examples document the validation API.

Validation is an Enterprise Edition feature.

The current examples demonstrate how the API is used and raise a feature-unavailable exception when executed with the Community Edition.

Example:

```bash
python -m examples.validate.validate_850
```

---

# respond Examples

Business response examples demonstrate generation of business documents in response to incoming transactions.

Examples include operations such as:

- 850 → 855 Purchase Order Acknowledgment
- 837 → 277 Claim Acknowledgment

Business responses are an Enterprise Edition feature.

Current examples document the API and raise a feature-unavailable exception when executed with the Community Edition.

Example:

```bash
python -m examples.respond.respond_850
```

---

# json_to_edi Examples

These examples demonstrate converting normalized JSON back into EDI.

JSON-to-EDI conversion is an Enterprise Edition feature.

Current examples document the API and raise a feature-unavailable exception when executed with the Community Edition.

Example:

```bash
python -m examples.json_to_edi.json_to_850
```

---

# sdk Examples

These examples demonstrate SDK-level functionality that is not specific to any EDI operation.

Current examples include:

| Example | Description |
|---------|-------------|
| `show_license_info.py` | Display the installed BerryWave EDI engine license information |

Example:

```bash
python -m examples.sdk.show_license_info
```

---

# Learning Path

If you are new to the SDK, a recommended order is:

1. `examples.edi_to_json.850_to_json`
2. `examples.edi_to_json.850_to_json_pretty`
3. `examples.edi_to_json.850_to_json_file`
4. `examples.acknowledge.acknowledge_850`
5. `examples.sdk.show_license_info`

After becoming familiar with the Community Edition features, the Enterprise Edition examples illustrate the APIs that become available when those capabilities are licensed.