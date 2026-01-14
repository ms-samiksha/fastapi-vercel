# FastAPI on Vercel 🚀

A minimal FastAPI project deployed on **Vercel** to test API hosting, routing, and performance (latency + uptime tracking).

## ✨ Features
- FastAPI backend (Python)
- Vercel deployment-ready structure
- Simple API endpoint for testing
- JSON-based latency/uptime logs

## 🧱 Tech Stack
- Python
- FastAPI
- Vercel

## 📁 Project Structure
fastapi-vercel/
├── api/
│ ├── index.py
│ └── q-vercel-latency.json
├── requirements.txt
└── vercel.json

bash
Copy code

## ▶️ Run Locally
1. Clone the repo:
bash
git clone https://github.com/ms-samiksha/fastapi-vercel.git
cd fastapi-vercel
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Start the server:

bash
Copy code
uvicorn api.index:app --reload
Open:

http://127.0.0.1:8000

🔗 Deployment
This project is structured to work with Vercel Python serverless functions.

📌 Notes
This repo was created to practice backend deployment and understand how FastAPI behaves in a serverless environment.
