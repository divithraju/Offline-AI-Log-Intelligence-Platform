# Offline AI Log Intelligence Platform

An offline, enterprise-style AI system that analyzes application logs using Ollama (local LLM), FastAPI, and React.
This project is designed to demonstrate system design, AI integration, and production-level thinking.

# Key Features

🔒 100% Offline AI (No cloud APIs, no data leakage)

🧠 Local LLM using Ollama (llama3)

⚙️ FastAPI backend for high-performance APIs

📜 Rule-based + AI hybrid analysis

🖥 React frontend for interactive querying

🧩 Modular, clean, interview-ready codebase

# How It Works

User pastes application logs in the React UI

User asks a natural language question (e.g., Why did the service crash?)

Logs are pre-processed and filtered using rule-based parsing

Important log segments are sent to Ollama (local LLM)

AI generates structured insights (root cause, frequency, recommendations)

Results are returned as JSON and displayed in the UI

 # Tech Stack

LLM: Ollama (llama3)

Backend: FastAPI (Python)

Frontend: React + Vite

AI Strategy: Rule-based + LLM hybrid

# Limitations

Large log files require batching

Domain-specific logs may need prompt tuning

# Future Enhancements

Authentication & RBAC

Docker & docker-compose

ElasticSearch integration

# Author

Divith Raju
B.Tech – Artificial Intelligence & Data Science

Cloud + on-prem hybrid deployment
