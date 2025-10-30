# SkillLink — Decentralized Credential Verification System

SkillLink is a Web3-powered platform that allows users to **verify, store, and share their professional credentials** securely using **Hedera Hashgraph** and **PostgreSQL (Neon DB)**.

This project was built for the **Hedera Africa Hackathon**, showcasing how blockchain can enhance **trust, transparency, and ownership of digital achievements**.

Pitch Deck: https://docs.google.com/presentation/d/1M4JZRe-ZCvU0twHipDZmg2_o_BJ5jWH_LGJRJk7HvEc/edit?usp=sharing 

My HDA certification link: https://certs.hashgraphdev.com/050bc06d-e061-4311-a953-35ea0ee33a3a.pdf
---

## 🚀 Vision
To empower individuals with self-sovereign control over their professional identity by creating a **tamper-proof, decentralized record** of skills and credentials.

---

## 🧩 Core Features
- **User Registration**: Create verified profiles with wallet-linked accounts.  
- **Credential Creation**: Add certificates, training records, or achievements.  
- **Blockchain Verification**: Store unique verification hashes on **Hedera Testnet**.  
- **On-Chain Proof**: Retrieve and confirm credentials via Hedera File IDs.  
- **Cloud Database**: Store structured user data in **Neon (PostgreSQL)**.  

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|-------------|
| Backend API | FastAPI (Python) |
| Blockchain | Hedera Hashgraph SDK |
| Database | Neon DB (PostgreSQL) |
| ORM | SQLAlchemy |
| Environment Management | Python-dotenv |
| Hashing | SHA-256 (via Python `hashlib`) |

---

## 🏗️ Project Structure
skilllink/
│
├── app/
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
│ ├── database.py
│ ├── routes/
│ │ ├── users.py
│ │ ├── credentials.py
│ │ └── verification.py
│ └── utils/
│ └── hedera_utils.py
│
├── requirements.txt
└── README.md

---

## ⚙️ Setup Guide

### 1. Clone Repository
```bash
git clone https://github.com/<your-username>/SkillLink.git
cd SkillLink

### 2. Create Virtual Environment
```bash 
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate







