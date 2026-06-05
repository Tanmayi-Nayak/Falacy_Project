# Week 1 Report: Environment Setup, Document Processing & Data Pipeline Foundation

## Project Overview

### Objective

The objective of this project is to develop an AI-powered logical fallacy detection system capable of analyzing textual arguments, identifying fallacious reasoning patterns, and providing explainable outputs. The system is being designed as a complete NLP pipeline that transforms unstructured documents into structured representations suitable for argument mining and machine learning.

### Supported Input Formats

* TXT
* DOCX

### Planned Outputs

* Detected logical fallacies
* Fallacy classification labels
* Fallacy location within the document
* Confidence scores
* Argument quality assessment
* Explanatory reasoning for predictions

### Example

**Input**

Everyone believes electric cars are perfect, therefore they must be perfect.

**Output**

* Fallacy: Appeal to Popularity (Bandwagon)
* Explanation: Popular acceptance does not establish factual correctness.
* Confidence Score: 0.92

## Week 1 Objectives

The first phase focused on building the foundational infrastructure required for all subsequent machine learning and NLP components.

Primary objectives included:

* Development environment configuration
* Text extraction pipeline development
* Text normalization and cleaning
* Sentence segmentation
* Structured data generation
* Version control integration
* Repository organization

At the conclusion of Week 1, a complete preprocessing pipeline was established that converts raw documents into machine-readable structured data.

## System Architecture

The current architecture consists of the following stages:

1. Document Input
2. Document Parser
3. Text Extraction Layer
4. Text Cleaning Layer
5. Sentence Segmentation Layer
6. Structured Data Generation
7. JSON Output

This architecture provides a modular foundation that can later be extended with:

* Tokenization
* Argument mining
* Claim detection
* Premise extraction
* Feature engineering
* Fallacy classification models
* Explainability modules

## Development Environment

### Core Technologies

| Technology | Purpose                      |
| ---------- | ---------------------------- |
| Python     | Primary development language |
| VS Code    | Development environment      |
| Git        | Version control              |
| GitHub     | Remote repository management |

### Environment Design Considerations

The development environment was configured with reproducibility and scalability in mind. All project dependencies are isolated from the global Python installation to ensure:

* Dependency consistency
* Cross-platform compatibility
* Easier deployment
* Reproducible experimentation
* Simplified collaboration

## Dependency Stack

The project currently integrates the following libraries:

### Backend Infrastructure

**FastAPI**

* REST API development
* Future model serving
* Endpoint creation for document analysis

**Uvicorn**

* ASGI server
* High-performance API execution

### Document Processing

**python-docx**

* DOCX parsing
* Paragraph extraction
* Heading extraction

**pdfplumber**

* PDF text extraction
* Page-level processing

**PyMuPDF**

* Advanced PDF parsing
* Metadata extraction
* Improved handling of complex PDF structures

### Natural Language Processing

**spaCy**

* Tokenization
* Sentence boundary detection
* Part-of-speech tagging
* Dependency parsing
* Named Entity Recognition

### Data Processing

**Pandas**

* Dataset construction
* Tabular data manipulation

**NumPy**

* Numerical operations
* Vectorized computations

### Machine Learning

**Scikit-learn**

* Traditional ML algorithms
* Data preprocessing utilities
* Evaluation metrics

**Transformers**

* Transformer-based NLP architectures
* Future fallacy classification models

**PyTorch**

* Deep learning framework
* Neural network implementation
* Transformer model training

## Dependency Management

Project dependencies are tracked using a requirements file.

Benefits include:

* Reproducible environments
* Version consistency
* Easier deployment
* Simplified onboarding of contributors
* Reduced dependency conflicts

This establishes the foundation for future experimentation and model training workflows.

## Document Ingestion System

### Purpose

Machine learning models cannot directly process document files. Therefore, a document ingestion layer was implemented to convert multiple file formats into a unified textual representation.

### TXT Processing

Capabilities:

* Plain text reading
* UTF-8 content extraction
* Standardized text output

Output:

* Raw document text

### DOCX Processing

Capabilities:

* Paragraph extraction
* Heading extraction
* Structured content retrieval

Output:

* Combined textual representation of the document

### PDF Processing

Capabilities:

* Page-level extraction
* Multi-page document support
* Text aggregation

Output:

* Unified text stream

### Design Goal

Regardless of source format, every document is transformed into a standardized textual representation before entering the NLP pipeline.

This abstraction simplifies downstream processing and model integration.

## Text Preprocessing Pipeline

### Motivation

Raw text often contains inconsistencies that negatively affect NLP performance.

Common issues include:

* Irregular spacing
* Formatting artifacts
* Line break inconsistencies
* Encoding irregularities
* Extraction noise

### Cleaning Operations

Implemented preprocessing tasks include:

* Whitespace normalization
* Line break cleanup
* Text standardization
* Basic formatting normalization

### Benefits

* Improved downstream NLP accuracy
* Reduced noise
* More consistent feature generation
* Better dataset quality

## Sentence Segmentation

### Purpose

Logical fallacies frequently occur within individual statements or small groups of statements.

Analyzing an entire document as a single block of text would reduce granularity and negatively impact future classification performance.

### Implementation

Sentence segmentation was implemented using spaCy's sentence boundary detection system.

Each document is transformed into a sequence of sentences that can later be:

* Independently analyzed
* Annotated
* Classified
* Linked to argument structures

### Benefits

* Fine-grained analysis
* Easier annotation workflows
* Improved model training samples
* Better explainability

## NLP Foundation Using spaCy

spaCy was selected as the primary NLP framework due to its efficiency, modularity, and production readiness.

Current capabilities integrated into the project include:

### Tokenization

Splits text into linguistic units suitable for analysis.

Example:

Input:

AI is powerful.

Tokens:

* AI
* is
* powerful
* .

### Part-of-Speech Tagging

Provides grammatical information such as:

* Nouns
* Verbs
* Adjectives
* Adverbs

### Dependency Parsing

Captures grammatical relationships between words.

This will be useful for:

* Claim extraction
* Premise identification
* Argument structure analysis

### Named Entity Recognition

Identifies entities such as:

* People
* Organizations
* Locations
* Dates

These features will become increasingly important in future argument-mining stages.

## Structured Data Generation

### Output Format

Processed documents are exported into JSON structures.

Stored information may include:

* Document metadata
* Cleaned text
* Sentence lists
* Future annotations
* Model predictions

### Advantages

* Human-readable
* Machine-readable
* API-friendly
* Easily expandable
* Suitable for training datasets

JSON serves as the primary interchange format between pipeline stages.

## Version Control Infrastructure

### Git Integration

Git was configured to manage source code and project history.

Key capabilities include:

* Change tracking
* Snapshot management
* Branching
* Merging
* Rollback support

### GitHub Integration

GitHub serves as the remote repository platform.

Benefits include:

* Remote backup
* Collaboration
* Issue tracking
* Project documentation
* Continuous integration readiness

## Repository Structure

The project structure was organized to support future expansion.

Planned modules include:

* Document ingestion
* NLP preprocessing
* Dataset generation
* Argument mining
* Fallacy detection
* Model training
* API services
* Evaluation utilities

This modular architecture promotes maintainability and scalability as the system grows.

## Technical Skills Developed

### Software Engineering

* Project architecture design
* Repository organization
* Version control workflows

### Data Engineering

* Multi-format document ingestion
* Data normalization
* Structured data generation

### Natural Language Processing

* Text preprocessing
* Sentence segmentation
* Linguistic feature extraction
* spaCy pipeline integration

### Machine Learning Preparation

* Dataset pipeline development
* Data serialization
* Infrastructure preparation for model training

## Week 1 Deliverables

Completed deliverables include:

* Python development environment setup
* VS Code configuration
* Git and GitHub integration
* Virtual environment creation
* Dependency installation and management
* TXT document reader
* DOCX document reader
* PDF document reader
* Text extraction pipeline
* Text cleaning pipeline
* Sentence segmentation pipeline
* JSON export functionality
* Repository structure initialization
* NLP framework integration

## Week 1 Outcome

Week 1 successfully established the complete preprocessing foundation required for future machine learning development.

The system can now:

* Ingest multiple document formats
* Extract textual content
* Normalize and clean text
* Segment documents into sentences
* Generate structured JSON outputs
* Store data in a machine-learning-ready format

This infrastructure provides the basis for all future argument analysis and fallacy detection components.

## Next Phase: Week 2

Planned objectives for Week 2 include:

* Argument Mining
* Claim Detection
* Premise Detection
* Argument Structure Extraction
* Annotation Framework Design
* Dataset Construction
* Initial Fallacy Labeling Strategy
* Training Data Preparation

**Week 1 Status:** Foundation Complete ✅
