# 🚀 Offline AI Log Intelligence Platform

## 📌 Project Description

The **Offline AI Log Intelligence Platform** is a **production-style AI SaaS application** designed to analyze application logs and provide **intelligent, structured insights using a locally hosted Large Language Model (LLM)**.

This project simulates how real-world SaaS platforms process logs, apply rule-based logic, and combine it with AI reasoning to assist developers and SRE teams in **debugging, monitoring, and root-cause analysis** — all while running **fully offline**.

The primary goal of this project is to **demonstrate real-world backend + AI + system design skills**, making it highly relevant for **Software Engineer / Backend Engineer / AI Engineer roles**.

### Key Highlights

* End-to-end system (UI → API → AI Model)
* Uses **local LLM (Ollama + LLaMA 3)** — zero API cost
* Hybrid **Rule Engine + LLM** architecture
* Clean, scalable, interview-ready SaaS design
* Privacy-first: no cloud dependency

---

## 🧠 System Architecture

```
User (React UI)
     |
FastAPI API Gateway
     |
Log Pre-Processor
     |        \
Rule Engine   Ollama (LLaMA3 LLM)
     |           |
Merged Structured Insights
     |
Response back to UI
```

---

## 🛠️ Tech Stack & Why Chosen

### Backend

* **Python 3.10+** – Industry-standard language with strong AI & backend ecosystem
* **FastAPI** – High-performance, async-ready, production-grade API framework
* **Pydantic** – Robust request/response validation and schema enforcement

### AI / LLM

* **Ollama (LLaMA 3)**

  * Fully **offline LLM inference**
  * No paid APIs or rate limits
  * Demonstrates real LLM integration skills valued by companies

### Frontend

* **React.js** – Industry-leading frontend framework
* **Axios** – Clean and maintainable API communication

### DevOps / Tooling

* **Docker** – Reproducible, scalable local deployment
* **Git & GitHub** – Version control and project showcasing

✅ This stack closely mirrors **real SaaS architectures used by startups and MNCs in Bangalore**.

---

## ⚙️ Step-by-Step Setup Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/divithraju/Offline-AI-Log-Intelligence-Platform.git
cd Offline-AI-Log-Intelligence-Platform
```

---

### 2️⃣ Backend Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
# .venv\\Scripts\\activate  # Windows

pip install -r requirements.txt
```

---

### 3️⃣ Install & Run Ollama (Local LLM)

```bash
# Install Ollama (Linux / Mac)
curl -fsSL https://ollama.com/install.sh | sh

# Pull LLaMA 3 model
ollama pull llama3

# Start Ollama server
ollama serve
```

---

### 4️⃣ Start FastAPI Server

```bash
uvicorn main:app --reload
```

API will be available at:

```
http://127.0.0.1:8000
```

Swagger API Docs:

```
http://127.0.0.1:8000/docs
```

---

### 5️⃣ Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend runs at:

```
http://localhost:3000
```

---
## 👨‍💻 My Individual Contributions

* Designed **end-to-end SaaS architecture** from scratch
* Built a **FastAPI backend** with clean routing and validation
* Implemented **log pre-processing and rule-based analysis engine**
* Integrated **local LLM (Ollama + LLaMA 3)** for intelligent insights
* Designed a **hybrid Rule Engine + AI decision flow**
* Developed **React-based UI** for real-time interaction
* Containerized the application using **Docker**
* Wrote **production-quality README and setup documentation**

---

## 🎯 Why This Project Stands Out

✅ Uses **real LLM-based AI**, not mock logic
✅ Fully **offline & cost-free**
✅ Mirrors real **SaaS backend architecture**
✅ Clear separation of concerns

---

## 📌 Future Enhancements

* JWT-based authentication & authorization
* Multi-user and role-based access
* Database integration (PostgreSQL / MongoDB)
* Support for multiple LLMs (Mistral, Gemma, Phi)
* Cloud deployment (AWS / GCP)

---

## 📞 Contact

**Divith Raju**
🎓 B.Tech
📍 Bangalore, India

🔗 GitHub: [https://github.com/divithraju](https://github.com/divithraju)

