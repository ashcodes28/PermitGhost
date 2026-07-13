![Status](https://img.shields.io/badge/Status-In_Development-orange)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-purple)
![Digital Twin](https://img.shields.io/badge/Digital_Twin-Enabled-blueviolet)
![License](https://img.shields.io/badge/License-MIT-green)

# 👻 PermitGhost

> **AI-Powered Industrial Safety Intelligence Platform**
>
> *Detecting dangerous work permit overlaps before they become industrial disasters.*

---

## 🚧 Project Status

This project is currently under active development for the **Economic Times AI Hackathon 2026**.

### Current Progress

- ✅ System Architecture
- ✅ Repository Setup
- 🟡 Backend Development
- ⬜ Digital Twin Simulator
- ⬜ Multi-Agent AI Engine
- ⬜ RAG Knowledge Base
- ⬜ React Dashboard
- ⬜ Deployment

---

# 🚨 Why PermitGhost?

Industrial accidents are rarely caused by a single failure.

Instead, they occur when multiple independent activities interact in unexpected ways.

Imagine this situation inside a refinery:

- 🔥 Welding is underway.
- ☣️ A gas leak begins nearby.
- 👷 Workers enter the affected zone.
- ⚙️ A cooling pump unexpectedly fails.

Each event alone appears manageable.

Together, they become catastrophic.

Today's Permit-to-Work (PTW) systems simply validate paperwork.

They **do not continuously reason across permits, sensors, equipment, worker locations, and historical incidents.**

PermitGhost fills this missing intelligence layer.

---

# 🎯 Our Solution

PermitGhost creates a **real-time Digital Twin** of an industrial plant and continuously evaluates its safety using multiple AI agents.

Instead of asking

> "Is this permit valid?"

PermitGhost continuously asks

> **"Given everything happening inside this plant right now, is it still safe?"**

The platform combines:

- Active Work Permits
- Live Sensor Streams
- Worker Locations
- Equipment Health
- Historical Near-Miss Reports
- Industrial Safety Regulations

to predict compound risks before accidents occur.

---

# 🧠 Core Features

## 🚧 Intelligent Permit Analysis

- Detects overlapping work permits
- Identifies conflicting maintenance activities
- Tracks permit validity and scheduling conflicts

---

## 🌐 Digital Twin Simulation

A live virtual refinery containing

- Workers
- Equipment
- Pipelines
- Storage Tanks
- Sensors
- Active Work Permits

The Digital Twin continuously evolves as simulated events occur.

---

## 🤖 Multi-Agent AI

Rather than relying on a single AI model, PermitGhost uses specialized agents.

- 📄 Permit Intelligence Agent
- 📡 Sensor Intelligence Agent
- 📍 Worker Location Agent
- ⚙️ Equipment Health Agent
- 📚 Historical Incident (RAG) Agent
- 🧠 Risk Fusion Agent

Each agent focuses on one aspect of industrial safety before collaborating to produce a final decision.

---

## 📚 Explainable AI

Every alert answers three questions:

- **What happened?**
- **Why is it dangerous?**
- **What should be done next?**

Along with:

- Historical incident references
- Relevant safety regulations
- Confidence score
- Recommended mitigation steps

---

## 📊 Interactive Dashboard

- Live Plant Layout
- Active Work Permits
- Live Sensor Data
- Worker Locations
- AI Risk Timeline
- Incident Evidence Panel
- Real-Time Alerts

---

# 🏗️ System Architecture

```text
                     React Dashboard
                            │
                    Live WebSocket Updates
                            │
                     FastAPI Backend API
                            │
          ┌─────────────────┴─────────────────┐
          │                                   │
     PostgreSQL                     AI Intelligence Layer
          │                                   │
          │                         Multi-Agent System
          │                                   │
          │                          Digital Twin Engine
          │                                   │
          └──────────── Sensor Simulator ─────┘
```

---

# ⚙️ Tech Stack

### Frontend

- React
- Tailwind CSS
- React Flow
- WebSockets

### Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- pgvector

### AI

- LangGraph
- Retrieval-Augmented Generation (RAG)
- scikit-learn
- Python

### Digital Twin

- Custom Simulation Engine
- Sensor Simulator
- Event Generator

---

# 🚀 Project Workflow

```text
Digital Twin
      │
      ▼
Sensor & Event Simulation
      │
      ▼
Permit Ingestion
      │
      ▼
Multi-Agent Reasoning
      │
      ▼
Compound Risk Detection
      │
      ▼
Explainable AI
      │
      ▼
Supervisor Dashboard
```

---

# 🎬 Demo Scenario

1. Start the Digital Twin simulation.
2. Workers begin maintenance operations.
3. Multiple work permits become active.
4. A gas leak develops in Zone 4.
5. A hot-work permit activates nearby.
6. AI agents correlate permits, sensors, worker locations, and historical incidents.
7. PermitGhost detects a compound hazard.
8. The dashboard highlights the affected zone.
9. The system explains the risk and recommends immediate mitigation before work continues.

---

# 🗺️ Roadmap

- [x] Repository Setup
- [x] System Architecture
- [ ] Database Design
- [ ] FastAPI Backend
- [ ] Digital Twin Simulator
- [ ] Permit Management Engine
- [ ] Sensor Simulator
- [ ] Multi-Agent AI
- [ ] RAG Knowledge Base
- [ ] React Dashboard
- [ ] Live WebSockets
- [ ] Deployment
- [ ] Demo Video

---

# 🔮 Future Scope

- Computer Vision for worker tracking
- Wearable IoT integration
- Predictive accident forecasting
- Automatic permit suspension
- Shift handover intelligence
- Regulatory audit report generation
- Real SCADA integration
- 3D Digital Twin visualization

---

# 🌍 Vision

PermitGhost is more than a permit management application.

Our vision is to build an **AI Safety Intelligence Layer** capable of continuously understanding everything happening inside an industrial facility and preventing accidents before they occur.

---

## 🤝 Contributing

Contributions, suggestions, and feedback are always welcome.

---

## 📄 License

This project is licensed under the MIT License.