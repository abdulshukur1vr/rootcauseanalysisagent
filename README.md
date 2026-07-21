# AI-Powered Recursive Log Analysis Agent

## Overview

The **AI-Powered Recursive Log Analysis Agent** is designed to automate the analysis of support bundles delivered as nested TAR archives.

The agent recursively extracts archives, discovers log files located under `nvram2/log`, parses and correlates events across multiple logs, and uses AI to identify the most probable root cause of failures.

Instead of manually searching through hundreds of log files, engineers receive a concise report containing:

- Likely root cause
- Supporting evidence
- Timeline of events
- Critical errors
- Recommendations
- Confidence score

---

# Objectives

- Automatically extract nested TAR archives
- Preserve extracted data in timestamped directories
- Discover all log files under `nvram2/log`
- Parse heterogeneous log formats
- Build a unified chronological timeline
- Detect known error patterns
- Correlate events across multiple logs
- Use AI to infer probable root cause
- Generate a human-readable report

---

# System Architecture

```text
                    Input TAR
                        │
                        ▼
          ┌─────────────────────────┐
          │ Recursive Extractor      │
          └─────────────┬───────────┘
                        │
                        ▼
          ┌─────────────────────────┐
          │ Log Discovery Agent      │
          └─────────────┬───────────┘
                        │
                        ▼
          ┌─────────────────────────┐
          │ Log Parser              │
          └─────────────┬───────────┘
                        │
                        ▼
          ┌─────────────────────────┐
          │ Timeline Builder         │
          └─────────────┬───────────┘
                        │
          ┌─────────────┴────────────┐
          ▼                          ▼
 Pattern Detection          Event Correlation
          │                          │
          └─────────────┬────────────┘
                        ▼
              AI Root Cause Engine
                        │
                        ▼
               Report Generator
```

---

# Workflow

## Step 1 - Input Processing

The agent accepts:

- `.tar`
- `.tar.gz`
- `.tgz`

Example:

```
support_bundle.tar
```

---

## Step 2 - Recursive Extraction

The extractor performs:

- Untar archive
- Search for embedded TAR files
- Extract nested archives recursively
- Continue until no TAR files remain

Each extraction is stored inside a timestamped directory.

Example:

```
workspace/

    20260721_113015/

        extracted_files...
```

Timestamp format:

```
YYYYMMDD_HHMMSS
```

---

## Step 3 - Log Discovery

The agent recursively searches for

```
**/nvram2/log/**
```

Example

```
device1/
    nvram2/log/

device2/
    nvram2/log/

device3/
    nvram2/log/
```

Every discovered log file is indexed.

---

# Supported Log Types

Examples include

```
syslog

messages

kernel.log

dmesg

daemon.log

application.log

event.log

panic.log

crash.log
```

The architecture allows additional parsers to be added easily.

---

# Parsing Pipeline

Each log entry is normalized into a common structure.

Example

| Field | Description |
|--------|-------------|
| Timestamp | Event time |
| Severity | INFO/WARN/ERROR |
| Source | Kernel, Application, etc. |
| Message | Original log message |

Example

```
Timestamp : 12:14:11

Severity : ERROR

Source : kernel

Message : Disk timeout detected
```

---

# Timeline Builder

Events from every log are merged into a unified chronological timeline.

Example

```
12:14:11  Kernel        Disk timeout

12:14:13  Filesystem    EXT4 error

12:14:16  Database      Connection lost

12:14:18  Watchdog      System reboot
```

---

# Pattern Detection Engine

Before invoking AI, deterministic analysis detects common failures.

Examples

```
Kernel panic

Segmentation fault

Out of Memory

OOM Killer

Filesystem readonly

Disk full

I/O timeout

Stack trace

Watchdog reset

Authentication failure

TLS failure

Certificate expired

Core dumped

Database unavailable

Network timeout

Assertion failure
```

The detection engine is based on configurable regex rules.

---

# AI Root Cause Analysis

Rather than analyzing every log line, the AI receives:

- Critical events
- Error summaries
- Timeline
- Stack traces
- Pattern matches

The AI determines

- Most likely root cause
- Supporting evidence
- System impact
- Recommended next steps
- Confidence score

Example output

```
Root Cause

Disk I/O failure

Confidence

94%

Evidence

Repeated I/O timeout

Filesystem remounted readonly

Application crash

Watchdog reboot

Recommendation

Inspect storage device

Run SMART diagnostics

Replace failing disk if necessary
```

---

# Event Correlation

The AI correlates events occurring across multiple logs.

Example

```
12:10:11

Disk timeout

↓

Filesystem readonly

↓

Database crash

↓

Watchdog reboot
```

Instead of reporting four independent errors, the agent concludes

```
Underlying cause

Storage subsystem failure
```

---

# Report Generation

The final report contains

```
Support Bundle

Summary

Likely Root Cause

Timeline

Critical Errors

Warnings

Affected Components

Supporting Evidence

Recommendations

Confidence Score
```

Reports can be generated in

- Markdown
- HTML
- PDF
- JSON

---

# Project Structure

```
project/

│

├── extractor/

│      recursive_extractor.py

│

├── discovery/

│      log_discovery.py

│

├── parser/

│      parser.py

│      syslog_parser.py

│      kernel_parser.py

│

├── timeline/

│      timeline_builder.py

│

├── detector/

│      regex_patterns.py

│      detector.py

│

├── ai/

│      rootcause_agent.py

│

├── report/

│      report_generator.py

│

├── config/

│      settings.yaml

│

├── output/

│

└── README.md
```

---

# Technology Stack

| Component | Technology |
|------------|------------|
| Language | Python 3.11+ |
| Archive Extraction | tarfile |
| File Discovery | pathlib |
| Parsing | Regex + Custom Parsers |
| Timeline Storage | Pandas / SQLite / DuckDB |
| AI Engine | OpenAI GPT / Local LLM |
| Report Generation | Markdown / HTML / PDF |
| UI (Optional) | Streamlit |

---

# Future Enhancements

- Multi-threaded extraction
- Parallel log parsing
- Vector search over historical incidents
- Retrieval-Augmented Generation (RAG)
- Similar incident matching
- Automatic Jira ticket generation
- Slack / Teams notifications
- Interactive web dashboard
- Knowledge base integration
- Plugin architecture for vendor-specific log parsers

---

# Expected Benefits

- Eliminates manual log inspection
- Handles deeply nested support bundles
- Correlates events across multiple logs
- Reduces Mean Time To Resolution (MTTR)
- Produces consistent and repeatable analyses
- Highlights probable root causes with supporting evidence
- Generates actionable recommendations for support engineers

---

# License

This project is intended as a modular framework for automated log analysis and AI-assisted root cause investigation. It can be extended with custom parsers, detection rules, and AI models to support a wide range of products and environments.


RootCauseAnalysisAgent/
│
├── README.md
├── LICENSE
├── requirements.txt
├── run.sh
├── setup.py
├── pyproject.toml
├── .gitignore
├── config/
│   ├── config.yaml
│   └── logging.yaml
│
├── data/
├── output/
├── prompts/
│   ├── summarize_prompt.txt
│   └── rootcause_prompt.txt
│
├── src/
│   ├── main.py
│   ├── cli.py
│   ├── config.py
│   ├── logger.py
│   │
│   ├── extractor/
│   │   ├── recursive_extractor.py
│   │   └── archive_utils.py
│   │
│   ├── discovery/
│   │   └── log_discovery.py
│   │
│   ├── parsers/
│   │   ├── base_parser.py
│   │   ├── syslog_parser.py
│   │   ├── kernel_parser.py
│   │   ├── dmesg_parser.py
│   │   ├── panic_parser.py
│   │   └── generic_parser.py
│   │
│   ├── timeline/
│   │   └── timeline_builder.py
│   │
│   ├── detector/
│   │   ├── regex_patterns.py
│   │   └── pattern_detector.py
│   │
│   ├── ai/
│   │   ├── llm_client.py
│   │   ├── summarizer.py
│   │   ├── rootcause_agent.py
│   │   └── prompts.py
│   │
│   ├── reports/
│   │   ├── markdown_report.py
│   │   ├── html_report.py
│   │   └── pdf_report.py
│   │
│   └── utils/
│       ├── file_utils.py
│       ├── time_utils.py
│       └── constants.py
│
├── tests/
│   ├── test_extractor.py
│   ├── test_parser.py
│   ├── test_detector.py
│   └── test_ai.py
│
└── docs/
    └── architecture.md


# proposed project structure

RootCauseAnalysisAgent/
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── pyproject.toml
├── run.sh
├── analyze.py                 # Entry point
│
├── config/
│   ├── config.yaml
│   └── logging.yaml
│
├── input/
├── workspace/
├── output/
├── logs/
├── prompts/
│
├── src/
│   ├── __init__.py
│   │
│   ├── core/
│   │     config.py
│   │     logger.py
│   │     constants.py
│   │
│   ├── extractor/
│   │     recursive_extractor.py
│   │     archive_utils.py
│   │
│   ├── discovery/
│   │     log_discovery.py
│   │
│   ├── parser/
│   │     base_parser.py
│   │
│   ├── detector/
│   │     pattern_detector.py
│   │
│   ├── timeline/
|   |     models.py
│   │     timeline_builder.py
│   │
│   ├── ai/
│   │     llm_client.py
│   │
│   ├── report/
│   │     report_generator.py
│   │
│   └── utils/
│   |     filesystem.py
│   |     timestamp.py
|   |
|   ├── analyzer/
|   |     __init__.py
│   |     models.py
│   |     rules.py
│   └     rootcause_engine.py
│
└── tests/
        test_rootcause_engine.py
# technology stack

Technology Stack
Component	Package
Python	3.11+
CLI	argparse
YAML Config	pyyaml
Logging	logging
Data	pandas
Progress	tqdm
AI	openai
PDF	reportlab
HTML	jinja2
Testing	pytest
File Discovery	pathlib
Archive	tarfile


