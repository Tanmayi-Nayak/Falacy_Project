# WEEK 1 REPORT

## Fallacy Detection and Argument Assessment System

### Phase 1: Environment Setup, Document Processing, and Data Pipeline Foundation

---

# 1. Project Overview

## Problem Statement

The objective of this project is to develop an Artificial Intelligence system capable of analyzing textual arguments and identifying logical fallacies present within them.

Input formats:

* TXT
* DOCX
* PDF

Output:

* Detected fallacies
* Location of fallacies
* Confidence score
* Argument quality score

Example:

Input:

Everyone believes electric cars are perfect, therefore they must be perfect.

Output:

Fallacy:
Appeal to Popularity

Reason:
Popularity does not imply correctness.

---

# 2. Why Week 1 Exists

Before building Machine Learning models, a system must first be able to:

1. Read documents
2. Extract text
3. Clean text
4. Organize data
5. Store processed information

Without these capabilities, no AI model can function.

Week 1 therefore focuses entirely on building the foundation.

---

# 3. Software Installation

## Python

Python is the primary programming language used for:

* Data Science
* Machine Learning
* Deep Learning
* Natural Language Processing
* Backend Development

Verify installation:

PowerShell:

python --version

Expected:

Python 3.x.x

---

## Visual Studio Code

VS Code serves as the development environment.

Benefits:

* Syntax highlighting
* Debugging
* Git integration
* Extension ecosystem

Recommended Extensions:

* Python
* Pylance
* Jupyter
* GitLens
* Error Lens

---

## Git

Git is a Version Control System.

Purpose:

* Track code changes
* Restore previous versions
* Collaborate with teams
* Connect with GitHub

Verify:

git --version

---

# 4. Understanding Project Structure

Project Folder:

fallacy-detector/

data/
raw/
processed/

src/
ingestion/
preprocessing/
models/
api/

main.py

Explanation:

data/
Stores all datasets.

raw/
Original files.

processed/
Cleaned data.

src/
Contains source code.

ingestion/
Reading documents.

preprocessing/
Cleaning text.

models/
Machine Learning code.

api/
Backend services.

main.py
Program entry point.

This structure is common across most professional AI projects.

---

# 5. Virtual Environment

## Why Virtual Environments Exist

Different projects often require different package versions.

Example:

Project A:
numpy 1.25

Project B:
numpy 2.0

Without isolation, package conflicts occur.

Virtual environments solve this problem.

---

Create Environment

python -m venv venv

Activate

PowerShell:

venv\Scripts\activate

Successful activation:

(venv)

Every future AI project should use virtual environments.

---

# 6. Package Installation

Packages are reusable libraries.

Install:

pip install fastapi
pip install uvicorn
pip install python-docx
pip install pdfplumber
pip install PyMuPDF
pip install spacy
pip install pandas
pip install numpy
pip install scikit-learn
pip install transformers
pip install torch

Purpose of Each Package

FastAPI
Backend API creation

Uvicorn
Runs FastAPI server

python-docx
Reads Word documents

pdfplumber
Reads PDFs

PyMuPDF
Advanced PDF extraction

spaCy
Natural Language Processing

Pandas
Data manipulation

NumPy
Numerical computation

Scikit-learn
Machine Learning

Transformers
Modern NLP models

PyTorch
Deep Learning

---

# 7. Requirements File

Purpose:

Stores exact package versions.

Create:

pip freeze > requirements.txt

Benefits:

Recreate project anywhere.

Install later:

pip install -r requirements.txt

This is standard industry practice.

---

# 8. Document Ingestion

Concept:

Computers cannot understand PDFs directly.

They first need text extraction.

Document

↓

Raw Text

↓

Processing

This stage is called Ingestion.

---

TXT Reader

Reads plain text files.

Output:

String

---

DOCX Reader

Uses python-docx.

Reads:

* Paragraphs
* Headings
* Text

Output:

Single text string

---

PDF Reader

Uses pdfplumber.

Process:

PDF

↓

Pages

↓

Extract text from each page

↓

Combine pages

Output:

Single text string

---

# 9. Natural Language Processing Basics

What is NLP?

Natural Language Processing enables computers to understand human language.

Examples:

* ChatGPT
* Grammarly
* Google Translate
* Voice Assistants

Our project uses NLP to understand arguments.

---

# 10. Text Cleaning

Raw text often contains:

Extra spaces

Special symbols

Formatting issues

Example:

"Hello     world"

After cleaning:

"Hello world"

Benefits:

* Faster processing
* Better ML performance
* Easier analysis

---

# 11. Sentence Segmentation

Definition:

Breaking text into individual sentences.

Example:

Input:

I love AI. AI is useful.

Output:

Sentence 1:
I love AI.

Sentence 2:
AI is useful.

Why Important?

Most fallacies occur at sentence level.

---

# 12. spaCy

spaCy is a modern NLP framework.

Capabilities:

* Tokenization
* POS Tagging
* Dependency Parsing
* NER
* Sentence Detection

Example:

Text:

AI is powerful.

Tokens:

AI
is
powerful
.

Future Weeks will heavily use spaCy.

---

# 13. Saving Processed Data

After cleaning:

Save into JSON.

Example:

{
"sentences":[
"AI is powerful.",
"Everyone believes AI."
]
}

Benefits:

* Easy storage
* Easy model training
* Human readable

JSON is widely used in APIs and ML pipelines.

---

# 14. Program Flow

Current System Workflow

Document

↓

Reader

↓

Text Extraction

↓

Text Cleaning

↓

Sentence Segmentation

↓

JSON Export

This completes the preprocessing pipeline.

---

# 15. Git Fundamentals

What is Git?

Git tracks every code change.

Benefits:

* Undo mistakes
* Restore old versions
* Team collaboration

---

Initialize Repository

git init

Creates:

.git/

Git now tracks project changes.

---

Check Status

git status

Shows:

* Modified files
* New files
* Deleted files

---

Add Files

git add .

Stages all files.

---

Commit Changes

git commit -m "Initial project setup"

Creates a permanent snapshot.

---

View History

git log

Displays all commits.

---

# 16. GitHub Fundamentals

GitHub is cloud storage for Git repositories.

Benefits:

* Backup
* Collaboration
* Portfolio building

Workflow:

Local Project

↓

Git

↓

GitHub

---

Create Repository

GitHub Website

↓

New Repository

↓

Copy URL

Example:

https://github.com/username/fallacy-detector.git

---

Connect Local Project

git remote add origin REPOSITORY_URL

Verify:

git remote -v

---

Push Project

git branch -M main

git push -u origin main

Code is now stored on GitHub.

---

# 17. Essential PowerShell Commands

Current Directory

pwd

List Files

dir

Change Directory

cd foldername

Move Back

cd ..

Create Folder

mkdir foldername

Create File

New-Item filename.txt

Delete File

Remove-Item filename.txt

Delete Folder

Remove-Item foldername -Recurse

Clear Terminal

cls

Open VS Code

code .

---

# 18. Essential Git Commands Summary

Initialize Repository

git init

Check Status

git status

Stage Files

git add .

Commit

git commit -m "message"

View History

git log

Create Branch

git branch branchname

Switch Branch

git checkout branchname

Push

git push

Pull

git pull

Clone Repository

git clone URL

---

# 19. Skills Learned During Week 1

Software Engineering

* Project Structure
* Git
* GitHub

Python Development

* Virtual Environments
* Package Management

Data Engineering

* Data Ingestion
* Data Storage

NLP

* Text Processing
* Sentence Segmentation

Machine Learning Preparation

* Dataset Pipeline Design

These skills transfer directly to:

* AI Systems
* Chatbots
* Recommendation Systems
* Computer Vision Projects
* Cybersecurity ML Systems
* Predictive Maintenance Projects
* Robotics AI Applications

---

# 20. Week 1 Deliverables

Completed:

✓ Python Setup

✓ VS Code Setup

✓ Git Setup

✓ GitHub Setup

✓ Virtual Environment

✓ Dependency Installation

✓ TXT Reader

✓ DOCX Reader

✓ PDF Reader

✓ Text Cleaning

✓ Sentence Segmentation

✓ JSON Export

✓ Project Structure

Week 1 Status:
FOUNDATION COMPLETE

The project is now ready for Week 2:
Argument Mining, Claim Detection, Premise Detection, Dataset Construction, and Initial Fallacy Annotation.
