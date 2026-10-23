# 🦥 LazyScroll: The Offline AI Voice Chat & Inbox Summarizer

LazyScroll is a 100% offline, privacy-first AI agent built to reward laziness for the **Hacktoberfest 2026 Open-Source AI Challenge: Week 3 (Slow and Steady)**. It ingests massive, chaotic group chat logs or bloated mailboxes and distills them into an ultra-short, actionable 2-line summary. Combined with a localized native text-to-speech feedback layer, users can consume their essential daily updates hands-free without burning energy staring at pixels.

---

## 🚀 Key Features
* **Sloth-Mode Local Inference:** Powered locally by Google's open-weight `gemma2:2b` via Ollama core arrays at `localhost:11434`.
* **Privacy-Preserved Chat Parsing:** Chat histories and messy inboxes stay entirely local on your device hardware, safeguarding sensitive family and workplace logs.
* **Eyes-Free Audio Ingestion:** Strips markdown tags and streams summaries straight to headphones using native cross-platform system speech capabilities.

---

## 🛠️ Tech Stack & Dependencies
* **Language:** Python 3.10+
* **AI Architecture:** Google Gemma Open Weights Ecosystem (`gemma2:2b`)
* **Local Broker Pipeline:** Ollama Linkage API
* **Vocal Interface:** Local Cross-Platform Native OS Speech Layers

---

## ⚙️ Installation & Running the Sloth Core (Step-by-Step)

### 1. Fire up the Core Weights
Install the open engine from [ollama.com](https://ollama.com). Pull down Google's micro architecture model weights via your terminal:
```bash
ollama run gemma2:2b
```

### 2. Pull Package Dependencies
Establish core interaction arrays inside your terminal script:
```bash
python -m pip install ollama
```

### 3. Let Code Do The Work
Execute the script loop to compress clutter and trigger the native audio broadcast system:
```bash
python app.py
```
