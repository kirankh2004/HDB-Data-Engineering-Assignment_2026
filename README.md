
# HDB Data Engineering Assignment 2026

An end-to-end **PySpark ETL pipeline** for processing Singapore HDB Resale Flat transaction data. This project demonstrates a production-style data engineering workflow including data ingestion, validation, transformation, hashing of sensitive data, profiling, and loading processed datasets.

---

# Architecture

![Architecture](diagrams/architecture.png)

---

# Project Overview

This solution implements a modular ETL pipeline that:

- Downloads HDB resale datasets
- Validates incoming data
- Cleans invalid records
- Performs business transformations
- Hashes sensitive information
- Generates data profiling statistics
- Stores processed outputs

The project is designed following modular software engineering principles with separate components for configuration, ingestion, validation, transformation, profiling, and loading.

---

# Objectives

This project demonstrates the following data engineering concepts:

- Modular ETL pipeline design
- Data quality validation
- Data cleansing
- Business transformations
- Sensitive data protection using hashing
- Data profiling and reporting
- Configuration-driven execution

---

# Technology Stack

| Technology             | Purpose                     |
| ---------------------- | --------------------------- |
| Python 3               | Programming Language        |
| Apache Spark (PySpark) | Distributed Data Processing |
| Pandas                 | Data Manipulation           |
| PyYAML                 | Configuration Management    |
| Git & GitHub           | Version Control             |
| Jupyter Notebook       | Development & Testing       |


---

# Repository Structure

```
HDB-Data-Engineering-Assignment_2026/
│
├── config/
│   └── config.yaml
│
├── data/
│   ├── raw/
│   ├── cleaned/
│   ├── transformed/
│   ├── hashed/
│   └── failed/
│
├── diagrams/
│   └── architecture.png
│
├── notebooks/
│   └── HDB_ETL_Assignment.ipynb
│
├── reports/
│
├── src/
│   ├── cleaner.py
│   ├── config.py
│   ├── download.py
│   ├── hasher.py
│   ├── loader.py
│   ├── profiler.py
│   ├── spark_session.py
│   ├── transformer.py
│   ├── validator.py
│   └── writer.py
│
├── requirements.txt
└── README.md
```

---

# ETL Workflow

## 1. Data Ingestion

- Downloads HDB resale transaction datasets
- Reads source CSV files
- Stores datasets in Raw layer

---

## 2. Data Validation

Performs data quality checks including:

- Null value validation
- Mandatory field validation
- Schema validation
- Data type validation

Invalid records are redirected to the **Failed** folder.

---

## 3. Data Cleaning

- Removes duplicate records
- Standardizes values
- Handles missing data
- Produces cleaned dataset

---

## 4. Data Transformation

Business transformations include:

- Column standardization
- Derived columns
- Formatting
- Data enrichment

---

## 5. Data Hashing

Sensitive information is hashed before publishing processed data.

---

## 6. Data Profiling

Generates summary statistics including:

- Record count
- Null counts
- Data completeness
- Column profiling

---

## 7. Data Loading

Writes processed datasets into output folders:

- Cleaned
- Transformed
- Hashed
- Failed Records

---

# Features

✔ Modular ETL Architecture

✔ Configuration-driven execution

✔ PySpark Data Processing

✔ Data Validation Framework

✔ Data Cleaning Pipeline

✔ Business Data Transformation

✔ Sensitive Data Hashing

✔ Data Profiling

✔ Error Handling

✔ Git Version Control

✔ Production-style Project Structure

---

# Input Data

The project processes Singapore HDB resale flat transaction datasets.

Example attributes include:

- Month
- Town
- Flat Type
- Block
- Street Name
- Storey Range
- Floor Area
- Flat Model
- Lease Commence Date
- Remaining Lease
- Resale Price

---

# Output

The pipeline generates the following outputs:

```
data/
│
├── raw/
├── cleaned/
├── transformed/
├── hashed/
└── failed/
```

---

# Installation

Clone the repository

```bash
git clone git@github.com:kirankh2004/HDB-Data-Engineering-Assignment_2026.git
```

Move into the project

```bash
cd HDB-Data-Engineering-Assignment_2026
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

**macOS/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Pipeline

Execute the ETL pipeline in the following order:

```bash
python src/download.py
```

```bash
python src/loader.py
```

```bash
python src/validator.py
```

```bash
python src/cleaner.py
```

```bash
python src/transformer.py
```

```bash
python src/hasher.py
```

```bash
python src/profiler.py
```

```bash
python src/writer.py
```

---

# Configuration

Application settings are maintained in:

```
config/config.yaml
```

Configuration includes:

- Input paths
- Output paths
- Processing parameters
- Runtime settings

---

# Reports

The project generates profiling information under:

```
reports/
├── .gitkeep
└── data_profile.txt (generated after execution)
```

---

# Version Control

The project is managed using Git and GitHub.

Typical workflow:

```bash
git add .
git commit -m "Commit message"
git push origin main
```

---

# Future Improvements

Possible production enhancements include:

- Unit testing
- Integration testing
- Logging framework
- CI/CD Pipeline
- Docker containerization
- Airflow orchestration
- Delta Lake support
- Data Quality Dashboard
- Cloud deployment

---

# Author

**Kiran Kharatmal**

GitHub: <https://github.com/kirankh2004>

---

# Note

This repository contains the solution developed for the **HDB Data Engineering Assignment 2026**. It demonstrates a modular, production-inspired ETL pipeline implemented using PySpark and Python..