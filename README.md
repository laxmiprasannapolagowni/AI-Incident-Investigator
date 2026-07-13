# 🚨 AI Incident Investigator

An AI-powered software log analysis application built using **Python**, **Streamlit**, and **Google Gemini AI**.

The application helps developers and Site Reliability Engineers (SREs) analyze software log files, detect incidents, identify possible root causes, classify severity levels, visualize log statistics, and generate AI-assisted investigation reports.

---

# 📖 Project Overview

Modern software systems generate thousands of log entries every day, making manual log investigation time-consuming and error-prone.

**AI Incident Investigator** simplifies incident analysis by automatically:

- Parsing software log files
- Detecting INFO, WARNING, ERROR, and CRITICAL events
- Classifying incident severity
- Identifying possible root causes
- Visualizing log statistics
- Generating AI-assisted incident analysis using Google Gemini
- Creating downloadable incident reports

This project demonstrates the practical use of **Artificial Intelligence**, **Log Analysis**, and **Data Visualization** for real-world software incident investigation.

---

# ✨ Features

- 📂 Upload `.log` and `.txt` files
- 📊 Interactive log statistics dashboard
- 🚨 Automatic incident severity detection
- 📈 Incident distribution chart
- 🕒 Incident timeline
- 🔍 Possible root cause detection
- 🤖 AI-powered incident analysis using Google Gemini
- 📄 Downloadable incident report
- 💻 User-friendly Streamlit interface

---

# 🖥️ Application Workflow

```text
Upload Log File
        │
        ▼
Parse Log Entries
        │
        ▼
Calculate Statistics
        │
        ▼
Detect Severity
        │
        ▼
Identify Root Cause
        │
        ▼
Generate AI Analysis
        │
        ▼
Download Incident Report
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Streamlit | Web Application |
| Google Gemini AI | AI Incident Analysis |
| Pandas | Data Processing |
| Matplotlib | Data Visualization |
| Git | Version Control |
| GitHub | Source Code Hosting |

---

# 📁 Project Structure

```text
AI-Incident-Investigator/
│
├── app.py
├── ai_analyzer.py
├── log_parser.py
├── report_generator.py
├── requirements.txt
├── README.md
│
├── sample_logs/
│      └── database_incident.log
│
├── screenshots/
│      ├── home.png
│      ├── dashboard.png
│      ├── timeline.png
│      ├── root-cause.png
│      └── ai-analysis.png
│
└── .gitignore
```

---

# 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/laxmiprasannapolagowni/AI-Incident-Investigator.git
```

### Move into the project folder

```bash
cd AI-Incident-Investigator
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

### Run the application

```bash
streamlit run app.py
```

---

# 📷 Application Screenshots

## 🏠 Home Page

![Home](screenshots/home.png)

---

## 📊 Dashboard

![Dashboard](screenshots/dashboard.png)

---

## 🕒 Incident Timeline

![Timeline](screenshots/timeline.png)

---

## 🔍 Possible Root Cause

![Root Cause](screenshots/root-cause.png)

---

## 🤖 AI Analysis

![AI Analysis](screenshots/ai-analysis.png)

---

# 🎯 Use Cases

- Software Incident Investigation
- DevOps Monitoring
- Site Reliability Engineering (SRE)
- Application Log Analysis
- AI-assisted Root Cause Detection
- Production Issue Investigation

---

# 🔮 Future Improvements

- 📄 PDF Report Generation
- 📊 Interactive Charts
- 📁 Multi-file Log Analysis
- 📧 Email Notifications
- ⚡ Real-time Log Streaming
- ☁️ Cloud Deployment
- 🔐 User Authentication

---

# 👩‍💻 Author

**Polagowni Laxmiprasanna**

🎓 **B.Tech – Information Technology**  
🏫 **CMR Engineering College, Hyderabad**

📧 **Email**  
laxmiprasannapolagowni@gmail.com

🔗 **GitHub**  
https://github.com/laxmiprasannapolagowni

💼 **LinkedIn**  
https://www.linkedin.com/in/laxmiprasannapolagowni/
