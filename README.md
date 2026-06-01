# BioMethodExtractor

An LLM-powered biomedical literature mining tool for automatically extracting **wet-lab experimental methods**, **laboratory instruments**, and **standard protocols** from scientific PDF articles.

The system focuses exclusively on the **Materials and Methods** section of biomedical research papers and converts unstructured experimental descriptions into structured JSON and Excel outputs.

---

## Features

### Experimental Method Extraction

Automatically identifies wet-lab experimental techniques and extracts:

- Method name
- Experimental purpose
- Key procedural steps
- Structured workflow information

Example:

```json
{
  "name": "Western Blot",
  "purpose": "Detect protein expression levels",
  "steps": [
    "Protein extraction",
    "SDS-PAGE separation",
    "Transfer to PVDF membrane",
    "Primary antibody incubation",
    "Chemiluminescent detection"
  ]
}
```

---

### Instrument Identification

Extracts laboratory instruments and equipment mentioned in the Methods section.

Example:

```json
[
  {
    "name": "Flow Cytometer"
  },
  {
    "name": "Thermal Cycler"
  }
]
```

---

### Standards and Protocol Mining

Identifies:

- Institutional protocols
- SOPs
- ISO standards
- Manufacturer protocols
- Experimental guidelines

Example:

```json
[
  {
    "type": "Manufacturer Protocol",
    "description": "RNA extraction according to kit instructions",
    "reference": "Qiagen Handbook"
  }
]
```

---

### Structured Output

The extracted information is exported into:

- JSON format
- Excel (.xlsx) format

Excel sheets include:

| Sheet | Content |
|---------|---------|
| 实验方法 | Experimental methods |
| 仪器设备 | Instruments and equipment |
| 标准协议 | Standards and protocols |

---

## Workflow

```text
PDF Article
      │
      ▼
PDF Parsing
      │
      ▼
Materials & Methods Detection
      │
      ▼
LLM-based Information Extraction
      │
      ├── Experimental Methods
      ├── Instruments
      └── Standards / Protocols
      │
      ▼
JSON Output
      │
      ▼
Excel Report
```

---

## Project Structure

```text
BioMethodExtractor/
│
├── extractor.py
├── install.py
├── requirements.txt
├── .env
│
├── INPUT_ARTI/
│   └── paper.pdf
│
├── output/
│   ├── paper.json
│   └── paper_methods.xlsx
│
└── README.md
```

---

## Installation

### Requirements

- Python 3.8+
- OpenAI-compatible API
- DeepSeek API Key (default implementation)

Install dependencies:

```bash
pip install -r requirements.txt
```

Or run:

```bash
python install.py
```

---

## Configuration

Create a `.env` file:

```env
DEEPSEEK_API_KEY=your_api_key_here
MODEL_NAME=deepseek-chat
```

---

## Usage

### Single PDF Processing

```bash
python extractor.py
```

Select:

```text
[1] single pdf
```

Input:

```text
example.pdf
```

Output:

```text
output/
├── example.json
└── example_methods.xlsx
```

---

### Batch Processing

```bash
python extractor.py
```

Select:

```text
[2] batch folder
```

Provide a folder containing multiple PDF files.

The program will automatically:

1. Parse all PDFs
2. Extract experimental information
3. Generate JSON files
4. Export Excel reports

---

## Extraction Rules

The extractor follows several strict constraints:

### Included

- Wet-lab experimental methods
- Laboratory instruments
- Experimental protocols
- Standard operating procedures
- Guidelines and standards

### Excluded

- Abstract
- Introduction
- Results
- Discussion
- References
- Statistical analysis
- Bioinformatics workflows
- Computational methods
- Data processing pipelines

Only the **Materials and Methods** section is analyzed.

---

## Output Example

```json
{
  "experimental_methods": [
    {
      "name": "Western Blot",
      "purpose": "Protein detection",
      "steps": [
        "Protein extraction",
        "Gel electrophoresis",
        "Membrane transfer"
      ]
    }
  ],
  "instruments": [
    {
      "name": "Flow Cytometer"
    }
  ],
  "standards_protocols": [
    {
      "type": "Manufacturer Protocol",
      "description": "RNA extraction protocol",
      "reference": "Qiagen Handbook"
    }
  ],
  "materials_section_found": true
}
```

---

## Scientific Contribution

Unlike simple prompt writing, this project implements a structured prompt-engineering framework for biomedical information extraction.

The contribution includes:

- Section-aware extraction
- Domain-specific filtering
- Wet-lab method prioritization
- Structured reasoning constraints
- Automated JSON schema generation

These design principles improve reproducibility and reduce hallucinations during literature mining.

---

## Dependencies

Main libraries:

- pandas
- openai
- pypdf
- python-dotenv
- openpyxl

---

## Future Development

- Multi-model support (GPT, Claude, Gemini, DeepSeek)
- RAG-enhanced extraction
- Ontology-based method normalization
- Experimental workflow graph generation
- Knowledge graph construction
- Benchmark evaluation on biomedical corpora

---

## License

MIT License

---

## Citation

If you use BioMethodExtractor in academic research, please cite:

```bibtex
@software{BioMethodExtractor,
  title={BioMethodExtractor: LLM-based Extraction of Experimental Methods from Biomedical Literature},
  author={Your Name},
  year={2026},
  url={https://github.com/your-repository}
}
```
