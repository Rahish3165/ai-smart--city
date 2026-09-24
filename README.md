# Urban Pulse AI - Smart City Infrastructure Grid 🏙️⚡

An AI-powered smart city monitoring and incident prediction system. Urban Pulse AI aggregates municipal incidents, maps live infrastructure health, and provides AI-based visual diagnostics for rapid urban problem detection and resolution.

---

## 🌟 Key Features

- **Interactive Incident Heatmap**: Powered by Leaflet and OpenStreetMap with CartoDB dark basemaps, displaying live municipal reports across cities.
- **AI Visual Diagnostics**: Citizen reporting tool that analyzes uploaded images for urban infrastructure defects (potholes, water leaks, garbage overflows, structural cracks) with confidence scoring.
- **Smart Alerts Feed**: Live telemetry panel tracking severity, status (Predicted vs. Reported), and timestamps.
- **Responsive Modern UI**: Built with React 19, Tailwind CSS, and Lucide icons.
- **FastAPI Microservice**: High-performance asynchronous Python backend serving real-time incident data and handling image analysis payloads.

---

## 🏗️ Project Architecture

```
ai-smart--city/
├── backend/
│   ├── main.py            # FastAPI API server & image analysis endpoints
│   ├── mock_data.py       # Incident data generator (100+ urban records)
│   ├── database.json      # Local JSON database of municipal incidents
│   └── requirements.txt   # Python dependencies (FastAPI, Uvicorn, multipart)
├── frontend/
│   ├── src/
│   │   ├── components/    # MapDashboard, SmartAlertsSidebar, CitizenUpload
│   │   ├── pages/         # LandingPage
│   │   ├── App.jsx        # Routing & state management
│   │   └── main.jsx       # React application entrypoint
│   ├── index.html
│   ├── vite.config.js
│   └── package.json
└── vercel.json            # Vercel deployment configuration
```

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- **Node.js** (v18+) & **npm**
- **Python** (v3.10+) & **pip**
- **Git**

---

### 2. Backend Setup

```bash
# Navigate to the backend directory
cd backend

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Generate new mock incidents
python mock_data.py

# Start the FastAPI server
uvicorn main:app --reload --port 8000
```

The backend will be available at:
- **API URL**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Interactive Swagger Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 3. Frontend Setup

```bash
# In a new terminal, navigate to the frontend directory
cd frontend

# Install npm dependencies
npm install

# Start the Vite development server
npm run dev
```

The frontend dashboard will run at:
- **Frontend URL**: [http://localhost:5173](http://localhost:5173)

---

## 📡 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/heatmap-data` | Retrieves all active incidents and AI predictions |
| `POST` | `/api/analyze-image` | Accepts image upload for automated defect classification |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
