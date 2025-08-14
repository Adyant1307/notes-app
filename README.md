📓 Notes App – Full Stack Assignment

A secure, scalable full-stack Notes App built from scratch with Next.js (frontend) and FastAPI + MongoDB (backend), fully containerized with Docker.
This project follows strict coding discipline, performance optimization, and security best practices.


🚀 Features

Frontend (Next.js + Tailwind CSS)

Hand-coded responsive UI with Tailwind CSS (no pre-built libraries)

State management using Zustand / Redux

Axios / React Query for API fetching

SEO-friendly with meta tags and code-splitting

Optional animations with Framer Motion


Backend (FastAPI)

JWT authentication for secure user sessions

MongoDB integration (via Motor & Pydantic)

Clear modular folder structure

Password hashing with Passlib

Performance-optimized API endpoints


DevOps

Version control with Git and commit hygiene (feat:, fix:, refactor:)

Fully containerized with Docker Compose

Configurable via environment variables (.env)

Ready-to-deploy production setup


🛠 Tech Stack

Frontend: Next.js, Tailwind CSS, Zustand/Redux, Axios/React Query
Backend: FastAPI, MongoDB, Motor, Pydantic, Passlib, JWT
DevOps: Docker, Git, .env configuration


📂 Project Structure

notes-app/
│   docker-compose.yml
│   README.md
│   .gitignore
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── models/
│   │   └── auth/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env
│
└── frontend/
    ├── src/
    ├── package.json
    ├── tailwind.config.js
    ├── Dockerfile
    └── .env


⚙️ Installation & Running the App

1️⃣ Clone the Repository

git clone https://github.com/Adyant1307/notes-app.git
cd notes-app

2️⃣ Add Environment Variables

Create .env files in both backend and frontend folders.

Backend .env

MONGO_URI=mongodb://mongo:27017/notes_db
JWT_SECRET=your_jwt_secret
JWT_ALGORITHM=HS256

Frontend .env

NEXT_PUBLIC_API_URL=http://localhost:8000

3️⃣ Run with Docker

docker compose up --build

4️⃣ Access the App

Frontend: http://localhost:3000

Backend API Docs: http://localhost:8000/docs


🧪 Testing

Performance tests can be run using locust or k6 against /api routes.

API load testing should confirm response times <200ms for most requests.


📜 Commit Guidelines

Use structured commit messages:

feat: added user registration API
fix: corrected MongoDB connection URI
refactor: optimized state management in frontend


📌 Notes

No AI-generated code unless annotated

No reused public code without attribution

Backend & Frontend both follow clean architecture

Production-ready Docker setup


👤 Author
ADYANT KUMAR VERMA
adyantkumarverma@gmail.com
