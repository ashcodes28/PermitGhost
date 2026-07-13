![Status](https://img.shields.io/badge/Status-In_Development-orange)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-purple)
![Digital Twin](https://img.shields.io/badge/Digital_Twin-Enabled-blueviolet)
![RAG](https://img.shields.io/badge/RAG-Industrial_Knowledge_Base-darkgreen)
![MQTT](https://img.shields.io/badge/MQTT-IoT-orange)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)
![License](https://img.shields.io/badge/License-MIT-green)

# 👻 PermitGhost

> **AI-Powered Industrial Safety Intelligence Platform**
>
> Detecting dangerous work permit overlaps before they become industrial disasters.

---

## 🚨 The Problem

Industrial accidents are rarely caused by a single failure. They occur when multiple independent activities create an unforeseen chain of events.

Imagine:

- 🔥 Hot work (welding) is underway.
- ☣️ A toxic gas leak begins nearby.
- 👷 Workers enter the affected area.
- ⚙️ A critical pump fails.

Each event may appear safe in isolation, but together they create a catastrophic hazard.

Current Permit-to-Work (PTW) systems only validate individual permits—they **do not understand compound risk**.

**PermitGhost** fills this missing intelligence layer.

---

# 🎯 Our Solution

PermitGhost is an AI-powered Industrial Safety Intelligence Platform that continuously monitors:

- Active Work Permits
- Live IoT Sensor Streams
- Worker Locations
- Equipment Health
- Historical Incident Reports
- Industrial Safety Regulations

The platform builds a **real-time Digital Twin** of the plant and uses **multi-agent AI reasoning** to detect dangerous combinations before accidents occur.

Instead of asking:

> "Is this permit valid?"

PermitGhost continuously asks:

> **"Is everything happening in this plant still safe?"**

---

# 🧠 Core Features

### 🚧 Intelligent Permit Analysis
- Detects overlapping and conflicting work permits.
- Tracks permit validity and scheduling conflicts.
- Identifies unsafe combinations of simultaneous activities.

### 🌐 Digital Twin Simulation
- Real-time virtual model of an industrial plant.
- Simulated workers, machinery, permits, and IoT sensors.
- Dynamic risk propagation across the facility.

### 🤖 Multi-Agent AI
Specialized AI agents collaborate to evaluate safety:

- Permit Intelligence Agent
- Sensor Intelligence Agent
- Worker Location Agent
- Equipment Health Agent
- Historical Incident (RAG) Agent
- Risk Fusion Agent

### 📡 Live Sensor Monitoring
Continuously processes:

- Gas concentration
- Temperature
- Pressure
- Oxygen levels
- Toxic gas detection

### 📚 Explainable AI + RAG
Every alert includes:

- Root cause analysis
- Similar historical incidents
- Relevant industrial safety regulations
- Recommended mitigation actions

### 📊 Interactive Dashboard
- Live plant map
- Active permits
- Sensor visualization
- AI-generated risk timeline
- Incident evidence panel

---

# 🏗️ System Architecture

```text
                   React Dashboard
                          │
                  Live WebSocket Updates
                          │
                  FastAPI Backend API
                          │
          ┌───────────────┴────────────────┐
          │                                │
      PostgreSQL                    AI Intelligence Layer
          │                                │
          │                        Multi-Agent System
          │                                │
          │                        Digital Twin Engine
          │                                │
          └────────────Sensor Simulator────┘
```

---

# 🛠️ Tech Stack

## Frontend
- React
- Tailwind CSS
- React Flow
- WebSockets

## Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- pgvector

## AI
- LangGraph
- RAG
- scikit-learn
- Python

## Digital Twin
- Custom Simulation Engine
- MQTT Sensor Simulation
- Real-time Event Generator

---

# 📂 Project Structure

```text
PermitGhost/

├── backend/
├── frontend/
├── ai_engine/
├── digital_twin/
├── data/
├── docs/
├── tests/
└── scripts/
```

---

# 🚀 Planned Workflow

```
Digital Twin
      ↓
Live Sensor Streams
      ↓
Permit Ingestion
      ↓
Multi-Agent AI Reasoning
      ↓
Compound Risk Detection
      ↓
Explainable Alert Generation
      ↓
Supervisor Dashboard
```

---

# 🎬 Demo Scenario

1. Launch the Digital Twin simulation.
2. Workers begin maintenance activities.
3. Multiple work permits become active.
4. A simulated gas leak develops.
5. Hot work starts in the affected zone.
6. AI agents detect a dangerous compound risk.
7. PermitGhost generates a human-readable alert with supporting evidence.
8. Supervisor receives mitigation recommendations before an accident occurs.

---

# 🔮 Future Roadmap

- CCTV-based worker tracking using Computer Vision
- Wearable IoT integration
- Predictive accident forecasting
- Automatic permit suspension
- Shift handover intelligence
- Regulatory audit generation
- Real SCADA integration
- 3D Digital Twin

---

# 🌍 Vision

Our goal is not simply to digitize industrial permits.

Our goal is to build an AI safety intelligence layer that enables industrial facilities to prevent accidents before they happen.

---

## 📄 License

This project is currently under active development for research and hackathon purposes.