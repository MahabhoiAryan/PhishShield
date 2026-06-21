# 🛡️ PhishShield – Email Threat Detection System ⚔️

PhishShield is a web-based Email Threat Detection System designed to analyze suspicious emails and identify potential phishing indicators. The system performs multi-layer analysis on email content, URLs, sender information, email subjects, and headers to help users assess email risks before interacting with them.

Users can either paste email content directly into the application or upload `.eml` email files for analysis. The system extracts relevant information, calculates a risk score, classifies the threat level, and presents the findings through an interactive dashboard.

**Project Status:** Work In Progress

---

# 📸 Screenshots

### Dashboard Home Page

![Dashboard](dummy text file\dashboard-report.png)

### Threat Analysis Report

![Analysis Report](dummy text file\main-landing.png)

---

# 🏗️ Project Architecture

```text
PhishShield
│
├── Flask Web Application
│
├── Email Input Layer
│   ├── Manual Email Text Input
│   └── EML File Upload
│
├── Email Processing Layer
│   ├── EML Parser
│   ├── Subject Analysis
│   ├── Header Analysis
│   ├── Sender Analysis
│   ├── URL Analysis
│   └── Keyword Detection
│
├── Risk Scoring Engine
│
├── Threat Summary Generator
│
├── SQLite Database Logging
│
└── Dashboard Reporting Interface
```

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/your-username/PhishShield.git
cd PhishShield
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install flask
```

## 5. Run Application

```bash
python app.py
```

## 6. Open Browser

```text
http://127.0.0.1:5000
```

---

# 🚀 How To Use

### Option 1: Analyze Email Text

1. Open the application.
2. Paste suspicious email content into the text box.
3. Click **Analyze Email**.
4. Review the generated threat report.

### Option 2: Analyze EML File

1. Open the application.
2. Click **Choose File**.
3. Select a valid `.eml` file.
4. The email content will automatically appear in the text box.
5. Click **Analyze Email**.
6. Review the threat analysis dashboard.

---

# 📊 Current Detection Capabilities

### Keyword-Based Threat Detection

Detects suspicious phishing-related terms such as:

- Urgent
- Verify
- Suspended
- Immediately
- Account
- Password

### URL Analysis

- Extracts URLs from email content
- Identifies suspicious domains
- Flags potentially malicious links

### Sender Analysis

- Examines sender information
- Detects suspicious sender patterns

### Subject Line Analysis

- Reviews email subject lines
- Detects common phishing indicators

### Header Analysis

Analyzes email headers including:

- Reply-To
- Return-Path
- Received

### Risk Scoring

Generates:

- Risk Score
- Risk Level Classification
  - LOW
  - MEDIUM
  - HIGH

### Threat Summary

Provides a summarized explanation of the detected findings.

### Scan History Storage

Stores scan records using SQLite database including:

- Sender
- Risk Level
- Risk Score
- Scan Timestamp

---

# 🛠️ Technologies Used

### Backend

- Python
- Flask

### Database

- SQLite

### Frontend

- HTML5
- CSS3
- JavaScript

### Email Processing

- Python Email Parsing Libraries

### Development Tools

- VS Code
- Git
- Virtual Environment (venv)

---

# ⚠️ Disclaimer

PhishShield is intended for educational, research, and cybersecurity learning purposes only.

The analysis results are based on implemented detection rules and should not be considered a replacement for professional security solutions or enterprise email security platforms.

Users should always perform additional verification before making security-related decisions based on the generated results.
