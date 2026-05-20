Biomedical Paper Method and Logic Extractor

Introduction

This project contains a set of automated scripts used to extract experimental methods, instruments, standard protocols, and logical causal chains from biomedical research papers (PDF or text). It utilizes Large Language Models (LLM) for information extraction and converts the results into structured JSON and CSV formats for subsequent analysis.

Key Features

PDF and Text Support: Supports direct reading of PDF files or CSV text lists.
LLM Driven: Based on DeepSeek or OpenAI API for intelligent extraction.
Method Extraction: Focuses on extracting experimental steps, instruments, and standards from the "Materials and Methods" section.
Logic Chain Analysis: Automatically builds causal edges and logic flowcharts.
Multi-format Output: Generates JSON full data, CSV simplified tables, and text summary reports.

Installation

Environment Requirements

Python 3.8 or higher
pip package manager

Library Dependencies:
pandas
openai
pypdf

Usage

This project contains two main scripts: pdf.py (extraction) and jsonTocsv.py (conversion).

Step 1: Configure API Key

Keep the default API key in config.env or replace it with your own key:

Step 2: Run Extraction Script
Supports processing single PDF

Process PDF file:
python pdf.py

Convert JSON to CSV

Output Files:

output/filename.json: Full extraction results
output/filename_results.csv: Simplified results table

Step 3: Conversion and Summary
Use jsonTocsv.py to convert JSON results into more readable logic chain CSV and text reports.

Default processes JSON files in the current directory:
python jsonTocsv.py

Or specify file path:
python jsonTocsv.py "output/Swift_et_al_2024.json"

Prompt Template
In pdf.py, you can customize the prompt_template. The current template focuses on extracting wet-lab methods.

Model Selection
Defaults to deepseek-chat, can be modified to other models compatible with the OpenAI format.

File Structure

Project Root

pdf.py: Main extraction script
jsonTocsv.py: Format conversion script
requirements.txt: Dependency list
input.pdf: Input PDF file (example)
output/: Output directory
*.json: Raw extraction data

Notes

Model Selection: This code uses the openai package to interface with Deepseek and Qwen models; pay attention when changing to other model APIs.
API Costs: Using LLM API will incur costs; please monitor token consumption.
Privacy Protection: Do not upload PDFs containing sensitive unpublished data to public APIs.
Encoding Issues: Ensure all files use UTF-8 encoding to avoid Chinese garbled text.

License

This project is licensed under the MIT License.

Contributing

Issues and Pull Requests are welcome to improve extraction results or add new features.

Contact

If you have questions, please contact via GitHub Issues


AI Use Declaration

This project utilizes Large Language Models (LLM) via API for text extraction and analysis. 
Purpose: Debugging, script drafting, and natural language processing (extraction of methods from text).

Tools: DeepSeek API, Qwen  API and OpenAI Python library.

Human Oversight: All outputs were verified by the author, and prompt engineering was manually refined.




Chinese version:

生物医学论文方法与逻辑提取器

简介

本项目包含一套自动化脚本，用于从生物医学研究论文（PDF 或文本）中提取实验方法、仪器、标准协议以及逻辑因果链。它利用大语言模型（LLM）进行信息抽取，并将结果转换为结构化的 JSON 和 CSV 格式，便于后续分析。

主要特性

PDF 和文本支持：支持直接读取 PDF 文件或 CSV 文本列表。
LLM 驱动：基于 DeepSeek 或 OpenAI API 进行智能提取。
方法提取：专注提取“材料与方法”部分的实验步骤、仪器和标准。
逻辑链分析：自动构建因果边（Causal Edges）和逻辑流程图。
多格式输出：生成 JSON 完整数据、CSV 简化表及文本总结报告。
安装

环境要求

Python 3.8 或更高版本
pip 包管理器

环境库依赖：
pandas
openai
pypdf



使用方法

本项目包含两个主要脚本：pdf.py (提取) 和 jsonTocsv.py (转换)。

第一步：配置 API 密钥


在 config.env保留默认api key或替换为自己的key：


第二步：运行提取脚本
支持处理单个 PDF

处理 PDF 文件：
python pdf.py

转换json至csv

输出文件：

output/filename.json: 完整提取结果
output/filename_results.csv: 简化结果表

第三步：转换与总结
使用 jsonTocsv.py 将 JSON 结果转换为更易读的逻辑链 CSV 和文本报告。

默认处理当前目录下的 JSON 文件：
python jsonTocsv.py

或指定文件路径：
python jsonTocsv.py "output/Swift_et_al_2024.json"

提示词模板
在 pdf.py 中可以自定义 prompt_template。当前模板专注于提取湿实验（Wet-lab）方法。

模型选择
默认使用 deepseek-chat，可修改为其他兼容 OpenAI 格式的模型。

文件结构

Project Root

pdf.py: 主提取脚本
jsonTocsv.py: 格式转换脚本
requirements.txt: 依赖列表
input.pdf: 输入 PDF 文件 (示例)
output/: 输出目录
*.json: 原始提取数据

注意事项
模型选择：本代码使用openai软件包对接Deepseek和Qwen模型，更换其他模型API需要注意
API 成本：使用 LLM API 会产生费用，请注意 token 消耗。
隐私保护：不要上传包含敏感未发表数据的 PDF 到公共 API。
编码问题：确保所有文件使用 UTF-8 编码，避免中文乱码。

许可证

本项目采用 MIT 许可证。

贡献

欢迎提交 Issue 和 Pull Request 来改进提取效果或添加新功能。

联系方式

如有问题，请通过 GitHub Issues 联系。