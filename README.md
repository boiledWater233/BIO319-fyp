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
# AI Usage Statement 

This project was developed with the assistance of Large Language Models (LLMs), which were used as productivity and development support tools during the project lifecycle.

AI-assisted activities may include, but are not limited to:

- Code review and optimization suggestions
- Prompt design and refinement
- Documentation drafting and editing
- Software architecture discussions
- README and technical documentation generation

All core research ideas, system design decisions, implementation, testing, validation, and final outputs were completed and verified by the project author.

The AI tools used in this project are considered development aids rather than contributors. The project author assumes full responsibility for the accuracy, integrity, and originality of all code, documentation, and research outcomes.

### AI Tools Potentially Used

- OpenAI ChatGPT
- DeepSeek
- GitHub Copilot (if applicable)

### Transparency and Reproducibility

To promote transparency and reproducibility:

- Prompts used for information extraction are publicly available in the source code.
- Data processing workflows are fully inspectable.
- Experimental outputs can be reproduced using the same inputs and configurations.
- All AI-generated content has been reviewed and validated by the author.

# BioMethodExtractor

一个基于大语言模型（LLM）的生物医学文献信息提取工具，用于从科研论文 PDF 中自动识别并提取：

- 湿实验方法（Wet-lab Methods）
- 实验仪器设备（Instruments）
- 标准规范与实验协议（Standards & Protocols）

本项目专注于论文的 **Materials and Methods（材料与方法）** 部分，将非结构化实验描述转换为结构化 JSON 和 Excel 数据，便于文献调研、实验复现和知识库构建。

---

# 功能特点

## 实验方法提取

自动识别论文中的核心湿实验技术，并提取：

- 方法名称
- 实验目的
- 关键实验步骤
- 结构化流程信息

示例：

```json
{
  "name": "Western Blot",
  "purpose": "检测目标蛋白表达水平",
  "steps": [
    "蛋白提取",
    "SDS-PAGE电泳",
    "转膜",
    "一抗孵育",
    "化学发光检测"
  ]
}
```

---

## 仪器设备识别

自动识别实验过程中使用的仪器设备。

示例：

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

## 标准协议提取

自动识别：

- 实验标准
- SOP（标准操作流程）
- ISO标准
- 厂商实验方案
- 机构实验规范

示例：

```json
[
  {
    "type": "Manufacturer Protocol",
    "description": "按照试剂盒说明书进行RNA提取",
    "reference": "Qiagen Handbook"
  }
]
```

---

## 结构化输出

提取结果可自动导出为：

- JSON格式
- Excel格式（.xlsx）

Excel文件包含以下工作表：

| 工作表 | 内容 |
|----------|----------|
| 实验方法 | 实验技术与关键步骤 |
| 仪器设备 | 论文涉及仪器 |
| 标准协议 | 实验标准与规范 |

---

# 工作流程

```text
科研论文 PDF
       │
       ▼
PDF文本解析
       │
       ▼
定位 Materials & Methods
       │
       ▼
大模型信息提取
       │
       ├── 实验方法
       ├── 仪器设备
       └── 标准协议
       │
       ▼
JSON结果
       │
       ▼
Excel报表
```

---

# 项目结构

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

# 安装说明

## 环境要求

- Python 3.8+
- OpenAI兼容API
- DeepSeek API Key（默认实现）

安装依赖：

```bash
pip install -r requirements.txt
```

或者运行安装脚本：

```bash
python install.py
```

---

# 配置说明

创建 `.env` 文件：

```env
DEEPSEEK_API_KEY=your_api_key_here
MODEL_NAME=deepseek-chat
```

---

# 使用方法

## 单篇论文处理

运行：

```bash
python extractor.py
```

选择：

```text
[1] single pdf
```

输入PDF文件名：

```text
example.pdf
```

输出：

```text
output/
├── example.json
└── example_methods.xlsx
```

---

## 批量处理

运行：

```bash
python extractor.py
```

选择：

```text
[2] batch folder
```

输入包含多个PDF文件的文件夹路径。

程序将自动：

1. 读取所有PDF
2. 提取实验信息
3. 生成JSON结果
4. 导出Excel文件

---

# 提取规则

本工具遵循严格的信息筛选原则。

## 包含内容

- 湿实验方法
- 实验仪器设备
- 实验流程
- 标准操作规范
- 实验指南与标准

## 排除内容

- Abstract（摘要）
- Introduction（引言）
- Results（结果）
- Discussion（讨论）
- References（参考文献）
- 统计学分析
- 生物信息学分析
- 数据处理流程
- 计算方法与软件分析

仅分析论文中的 **Materials and Methods（材料与方法）** 部分。

---

# 输出示例

```json
{
  "experimental_methods": [
    {
      "name": "Western Blot",
      "purpose": "蛋白表达检测",
      "steps": [
        "蛋白提取",
        "电泳分离",
        "转膜检测"
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
      "description": "RNA提取说明书",
      "reference": "Qiagen Handbook"
    }
  ],
  "materials_section_found": true
}
```

---

# 科学贡献

本项目并非简单地利用提示词调用大模型，而是构建了一套面向生物医学文献的信息提取框架。

主要创新点包括：

- Materials & Methods章节自动定位
- 领域特异性信息过滤
- 湿实验优先提取策略
- 结构化Prompt Engineering设计
- 自动JSON Schema生成
- Excel结构化导出

相比传统关键词检索方法，本系统能够实现更加稳定、可复现的实验方法信息抽取，为科研知识挖掘提供支持。

---

# 依赖库

主要依赖：

- pandas
- openai
- pypdf
- python-dotenv
- openpyxl

---

# 未来工作

计划增加以下功能：

- GPT、Claude、Gemini等多模型支持
- RAG增强检索
- 实验方法标准化映射
- 实验流程图自动生成
- 生物医学知识图谱构建
- Benchmark评测体系

---

# 开源协议

MIT License

---

# 引用方式

如果本项目对您的研究工作有所帮助，请引用：

```bibtex
@software{BioMethodExtractor,
  title={BioMethodExtractor: 基于大语言模型的生物医学实验方法自动提取工具},
  author={Your Name},
  year={2026},
  url={https://github.com/your-repository}
}
```

---

# 致谢

感谢以下开源项目与工具：

- DeepSeek
- OpenAI SDK
- PyPDF
- Pandas
- OpenPyXL

本项目旨在探索大语言模型在生物医学文献挖掘与实验知识结构化中的应用。
