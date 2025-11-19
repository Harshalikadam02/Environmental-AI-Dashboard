# 🌍 NYC Environmental Risk Dashboard (DEP Dashboard)

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

**A real-time environmental monitoring and risk assessment dashboard powered by AI**

[Features](#-core-features) • [Architecture](#-system-architecture) • [Quick Start](#-development-steps) • [API](#-api-integration) • [Troubleshooting](#-troubleshooting-guide)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Project Structure](#-project-structure)
- [App Preview](#-app-preview)
- [Key Structures](#-key-structures)
- [System Architecture](#-system-architecture)
- [Web Interface](#-web-interface)
- [API Integration](#-api-integration)
- [Development Steps](#-development-steps)
- [Docker Deployment](#-docker-deployment)
- [Troubleshooting Guide](#-troubleshooting-guide)
- [Use Cases & Applications](#-use-cases--applications)
- [Author](#-author)

---

## 🎯 Overview

The **NYC Environmental Risk Dashboard** is an intelligent, real-time monitoring system designed for the NYC Department of Environmental Protection (DEP). It integrates air quality data (PM2.5, NO2, O3) with automated traffic volume counts to identify pollution hotspots, calculate composite risk scores, and provide actionable insights across NYC boroughs.

### Key Highlights

- 🤖 **AI-Powered Analytics**: Google Gemini 2.5 Flash integration for descriptive, predictive, and custom query analysis
- 🗺️ **Geospatial Visualization**: Interactive Leaflet.js maps with color-coded risk zones
- 📊 **Real-time Risk Scoring**: Composite algorithm (60% PM2.5, 40% traffic) with priority queue ranking
- 🚨 **Live Alert System**: Simulated pollution spike detection with audio/visual notifications
- 📈 **Advanced Visualizations**: Chart.js-powered analytics with bar charts, doughnut charts, and gauges

---

## 📁 Project Structure

### Directory Tree

```
DEP_Dashboard/
│
├── 📄 api.py                          # Flask REST API server
├── 📄 api_EXAMPLE.py                  # API template with placeholder credentials
├── 📄 index.html                      # Main dashboard frontend
├── 📄 index_EXAMPLE.html              # Frontend template
├── 📓 DataEngineering_Team_3.ipynb   # ETL pipeline & data processing notebook
├── 📄 PROJECT_SUMMARY.md              # Project documentation
├── 📄 System architecture.pdf         # Architecture diagrams
├── 📹 final project demo.mov          # Video demonstration
└── 📦 Team3_Project code and video.zip # Project archive
```

### Project Structure Chart

```
┌─────────────────────────────────────────────────────────────────┐
│                    DEP Dashboard Architecture                    │
└─────────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│   Data Layer  │    │  Backend API  │    │  Frontend UI  │
├───────────────┤    ├───────────────┤    ├───────────────┤
│ • Air Quality │    │ • Flask       │    │ • HTML5/CSS3  │
│   CSV Files   │───▶│ • PyMongo     │◀───│ • Tailwind    │
│ • Traffic     │    │ • CORS        │    │ • JavaScript  │
│   Counts      │    │ • REST API    │    │ • Chart.js    │
└───────────────┘    └───────────────┘    │ • Leaflet.js  │
        │                   │              │ • Gemini AI   │
        │                   │              └───────────────┘
        ▼                   ▼
┌───────────────┐    ┌───────────────┐
│  ETL Pipeline │    │   MongoDB     │
│  (Jupyter)    │───▶│   Atlas       │
│  • Pandas     │    │   Cloud DB    │
│  • Transform  │    └───────────────┘
│  • Load       │
└───────────────┘
```

### Component Breakdown

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **ETL Pipeline** | Jupyter Notebook, Pandas | Data extraction, transformation, and loading to MongoDB |
| **Backend API** | Flask, PyMongo | RESTful API serving environmental data |
| **Database** | MongoDB Atlas | Cloud-hosted document store for air quality & traffic data |
| **Frontend** | HTML5, Tailwind CSS, JavaScript | Interactive dashboard UI |
| **Visualization** | Chart.js, Leaflet.js | Charts, maps, and geospatial displays |
| **AI Engine** | Google Gemini 2.5 Flash | Intelligent analysis and predictions |

---

## 🎬 App Preview

### Video Demonstration

📹 **[Watch Full Demo Video](./final%20project%20demo%20.mov)**

*Note: The demo video showcases real-time risk assessment, AI-powered analytics, geospatial hotspot visualization, and live alert simulation.*

### Dashboard Features Preview

#### 🗺️ Geospatial Hotspots
- Interactive map with color-coded markers (Critical/High/Moderate/Low risk)
- Real-time location-based risk visualization
- Click markers for detailed zone information

#### 📊 Priority Queue
- Real-time ranking of areas requiring immediate attention
- Top 10 critical zones with risk scores and recommended actions
- Auto-updating based on live data

#### 🤖 AI Analyst
- **Descriptive Analysis**: Summarizes trends and identifies top risk zones
- **Predictive Analysis**: Forecasts pollution spikes with confidence levels
- **Custom Query**: Natural language interface for ad-hoc questions

#### 📈 Key Metrics
- Critical Risk Zones count
- Average Citywide PM2.5 levels
- High Congestion Zones identification
- Air Quality Gauge visualization

---

## 🔧 Key Structures

### Risk Scoring Algorithm

```python
# Risk Score Calculation
normalizedPM25 = min((avg_pm25 / 100) * 100, 100)
normalizedTraffic = min((avg_traffic / 1000) * 100, 100)
riskScore = (normalizedPM25 × 0.6) + (normalizedTraffic × 0.4)

# Status Classification
if riskScore >= 70:    → Critical  → "Dispatch Air Quality Mobile Unit"
elif riskScore >= 50:  → High      → "Schedule Inspection"
elif riskScore >= 30:  → Moderate  → "Monitor Closely"
else:                  → Low       → "Routine Check"
```

### Data Flow Architecture

```
┌─────────────┐
│  CSV Files  │
│  (Air/Traffic)│
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  ETL Pipeline│
│  (Pandas)   │
│  • Clean    │
│  • Transform│
│  • Merge    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  MongoDB    │
│  Atlas      │
│  Collection │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Flask API  │
│  /api/data  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Frontend   │
│  Dashboard  │
│  • Risk Calc│
│  • Visualize│
│  • AI Query │
└─────────────┘
```

### API Response Structure

```json
[
  {
    "Name": "Fine particles (PM 2.5)",
    "Measure Info": "Mean",
    "Geo Place Name": "Brooklyn",
    "Start_Date": "2024-01-01",
    "Data Value": 12.5,
    "Vol": 850,
    "Boro": "Brooklyn"
  }
]
```

### Frontend Risk Data Structure

```javascript
{
  name: "Brooklyn",
  lat: 40.6782,
  lng: -73.9442,
  pm25: 12.5,
  congestion_level: 850.0,
  riskScore: 65.3,
  status: "High",
  action: "Schedule Inspection"
}
```

---

## 🏗️ System Architecture

### High-Level Architecture Diagram

```
┌──────────────────────────────────────────────────────────────────────┐
│                         CLIENT LAYER                                 │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │                    Web Browser (Frontend)                      │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐      │  │
│  │  │   Map    │  │  Charts  │  │   AI     │  │  Alerts  │      │  │
│  │  │ (Leaflet)│  │(Chart.js)│  │(Gemini)  │  │  System  │      │  │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘      │  │
│  └───────────────────────────┬────────────────────────────────────┘  │
└──────────────────────────────┼───────────────────────────────────────┘
                               │ HTTP/REST
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│                         APPLICATION LAYER                            │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │                    Flask REST API Server                        │  │
│  │  ┌──────────────────────────────────────────────────────────┐  │  │
│  │  │  Route: GET /api/data                                    │  │  │
│  │  │  • CORS Enabled                                          │  │  │
│  │  │  • MongoDB Connection Pool                               │  │  │
│  │  │  • JSON Response Format                                  │  │  │
│  │  └──────────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────┬────────────────────────────────────┘  │
└──────────────────────────────┼───────────────────────────────────────┘
                               │ PyMongo Driver
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│                          DATA LAYER                                  │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │                    MongoDB Atlas (Cloud)                       │  │
│  │  ┌──────────────────────────────────────────────────────────┐  │  │
│  │  │  Database: myDatabase                                    │  │  │
│  │  │  Collection: air_quality_traffic                         │  │  │
│  │  │  • Air Quality Metrics (PM2.5, NO2, O3)                  │  │  │
│  │  │  • Traffic Volume Counts                                 │  │  │
│  │  │  • Geospatial Data                                       │  │  │
│  │  └──────────────────────────────────────────────────────────┘  │  │
│  └────────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────┘
                               ▲
                               │ ETL Pipeline
                               │
┌──────────────────────────────────────────────────────────────────────┐
│                         DATA SOURCE LAYER                            │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │  • Air_Quality_20251114.csv                                    │  │
│  │  • Automated_Traffic_Volume_Counts_20251114.csv                │  │
│  │  ┌──────────────────────────────────────────────────────────┐  │  │
│  │  │  Jupyter Notebook ETL                                    │  │  │
│  │  │  • Data Cleaning (Pandas)                                │  │  │
│  │  │  • Data Transformation                                   │  │  │
│  │  │  • Data Loading to MongoDB                               │  │  │
│  │  └──────────────────────────────────────────────────────────┘  │  │
│  └────────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────┘
```

### Technology Stack

#### Backend
- **Flask 2.0+**: Lightweight WSGI web application framework
- **PyMongo**: MongoDB driver for Python
- **Flask-CORS**: Cross-Origin Resource Sharing support
- **Python 3.8+**: Core programming language

#### Frontend
- **HTML5/CSS3**: Semantic markup and styling
- **Tailwind CSS**: Utility-first CSS framework
- **JavaScript (ES6+)**: Modern JavaScript features
- **Chart.js**: Data visualization library
- **Leaflet.js**: Open-source mapping library
- **Phosphor Icons**: Icon library

#### Data Processing
- **Pandas**: Data manipulation and analysis
- **Jupyter Notebook**: Interactive development environment
- **MongoDB Atlas**: Cloud-hosted NoSQL database

#### AI Integration
- **Google Gemini 2.5 Flash Preview**: Large language model for environmental analysis
- **Generative AI API**: RESTful interface for AI queries

---

## 🖥️ Web Interface

### Dashboard Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│                    NYC Environmental Risk Dashboard                  │
│                    DEP - Proactive Pollution Control                 │
│                    [SIMULATE LIVE ALERT] Button                      │
└─────────────────────────────────────────────────────────────────────┘

┌──────────────┐  ┌──────────────────────────────┐  ┌──────────────┐
│              │  │                              │  │              │
│  Priority    │  │     Geospatial Hotspots      │  │  Citywide    │
│  Queue       │  │     (Interactive Map)        │  │  Air Quality │
│              │  │                              │  │  (Gauge)     │
│  • Top 10    │  │                              │  │              │
│  • Risk      │  │                              │  │              │
│  • Actions   │  │                              │  │              │
│              │  │                              │  │              │
├──────────────┤  ├──────────────────────────────┤  ├──────────────┤
│              │  │     Traffic Patterns          │  │  Risk Factor │
│              │  │     (Bar Chart)               │  │  Analysis    │
│              │  │                              │  │  (Doughnut)  │
│              │  │                              │  │              │
│              │  ├──────────────────────────────┤  ├──────────────┤
│              │  │     AI Analyst                │  │  Key Metrics │
│              │  │     ┌──────┬──────┬──────┐   │  │              │
│              │  │     │Desc. │Pred. │Custom│   │  │  • Critical  │
│              │  │     └──────┴──────┴──────┘   │  │  • Avg PM2.5 │
│              │  │     [Analysis Results]        │  │  • Congestion│
│              │  │                              │  │              │
└──────────────┘  └──────────────────────────────┘  └──────────────┘
```

### UI Components

#### 1. **Priority Queue Panel** (Left Sidebar)
- Real-time ranked list of critical zones
- Color-coded status indicators
- Action recommendations per zone
- Scrollable list with top 10 priorities

#### 2. **Geospatial Hotspots** (Center - Top)
- Interactive Leaflet.js map
- Color-coded markers:
  - 🔴 **Red**: Critical (≥70)
  - 🟠 **Orange**: High (≥50)
  - 🟡 **Yellow**: Moderate (≥30)
  - 🟢 **Green**: Low (<30)
- Click markers for detailed popup information

#### 3. **Traffic Patterns Chart** (Center - Middle)
- Bar chart showing risk scores by borough
- Color-coded bars matching risk status
- Responsive design with Chart.js

#### 4. **AI Analyst Panel** (Center - Bottom)
- Three-tab interface:
  - **Descriptive**: Current state analysis
  - **Predictive**: Future risk forecasting
  - **Custom**: Natural language queries
- Real-time AI processing with loading indicators
- Formatted response display

#### 5. **Citywide Air Quality Gauge** (Right - Top)
- Circular progress indicator
- Real-time PM2.5 average display
- Animated SVG gauge

#### 6. **Risk Factor Analysis** (Right - Middle)
- Doughnut chart for top risk location
- PM2.5 (60%) vs Traffic (40%) breakdown
- Visual representation of risk composition

#### 7. **Key Metrics Panel** (Right - Bottom)
- Three KPI cards:
  - Critical Risk Zones count
  - Average Citywide PM2.5
  - High Congestion Zones count

### Interactive Features

- **Live Alert Simulation**: Click "SIMULATE LIVE ALERT" to trigger pollution spike demo
- **Map Interaction**: Click markers for detailed zone information
- **AI Query Interface**: Enter custom questions in natural language
- **Real-time Updates**: Dashboard refreshes data from API on load
- **Responsive Design**: Adapts to different screen sizes

---

## 🔌 API Integration

### API Endpoint

**Base URL**: `http://127.0.0.1:5001`

#### GET `/api/data`

Retrieves all environmental risk data from MongoDB.

**Request:**
```http
GET /api/data HTTP/1.1
Host: 127.0.0.1:5001
```

**Response:**
```json
[
  {
    "Name": "Fine particles (PM 2.5)",
    "Measure Info": "Mean",
    "Geo Place Name": "Brooklyn",
    "Start_Date": "2024-01-01",
    "Data Value": 12.5,
    "Vol": 850,
    "Boro": "Brooklyn"
  },
  ...
]
```

**Status Codes:**
- `200 OK`: Successfully retrieved data
- `500 Internal Server Error`: Database connection or query error

### API Implementation

```python
# api.py
from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import json_util
import json

app = Flask(__name__)
CORS(app)

MONGO_CONNECTION_STRING = 'mongodb+srv://...'

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        client = MongoClient(MONGO_CONNECTION_STRING)
        db = client['myDatabase']
        collection = db['air_quality_traffic']
        documents = list(collection.find({}, {'_id': 0}))
        json_data = json.loads(json_util.dumps(documents))
        return jsonify(json_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if 'client' in locals():
            client.close()
```

### Frontend API Integration

```javascript
// Fetch data from Flask API
async function loadDashboardData() {
    const response = await fetch('http://127.0.0.1:5001/api/data');
    const apiData = await response.json();
    const riskData = runRiskEngine(apiData);
    renderDashboard(riskData);
}
```

### CORS Configuration

The API includes CORS support to allow cross-origin requests from the frontend:

```python
from flask_cors import CORS
CORS(app)  # Enables CORS for all routes
```

---

## 🚀 Development Steps

### Prerequisites

- **Python 3.8+** installed
- **MongoDB Atlas** account (or local MongoDB instance)
- **Node.js** (optional, for package management)
- **Modern web browser** (Chrome, Firefox, Safari, Edge)

### Local Development Setup

#### Step 1: Clone Repository

```bash
git clone <repository-url>
cd DEP_Dashboard
```

#### Step 2: Install Python Dependencies

```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install flask flask-cors pymongo
```

**Alternative: Create `requirements.txt`**

```txt
flask>=2.0.0
flask-cors>=3.0.0
pymongo>=4.0.0
```

Then install:
```bash
pip install -r requirements.txt
```

#### Step 3: Configure MongoDB Connection

1. **Get MongoDB Atlas Connection String:**
   - Log in to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
   - Create a cluster (or use existing)
   - Go to "Connect" → "Connect your application"
   - Copy the connection string

2. **Update `api.py`:**
   ```python
   MONGO_CONNECTION_STRING = 'mongodb+srv://username:password@cluster.mongodb.net/myDatabase?retryWrites=true&w=majority'
   ```

   Or use environment variable:
   ```python
   import os
   MONGO_CONNECTION_STRING = os.getenv('MONGO_URI', 'your-default-connection-string')
   ```

#### Step 4: Load Data to MongoDB

1. **Open Jupyter Notebook:**
   ```bash
   jupyter notebook DataEngineering_Team_3.ipynb
   ```

2. **Run ETL Pipeline:**
   - Execute all cells in the notebook
   - Ensure CSV files are in the correct path
   - Verify data is loaded to MongoDB Atlas

3. **Verify Data:**
   ```python
   from pymongo import MongoClient
   client = MongoClient(MONGO_CONNECTION_STRING)
   db = client['myDatabase']
   collection = db['air_quality_traffic']
   print(collection.count_documents({}))
   ```

#### Step 5: Start Flask API Server

```bash
python api.py
```

**Expected Output:**
```
 * Running on http://127.0.0.1:5001
 * Debug mode: on
```

#### Step 6: Open Frontend Dashboard

1. **Open `index.html` in browser:**
   - Double-click `index.html`, or
   - Use a local server:
     ```bash
     # Python 3
     python -m http.server 8000
     
     # Then navigate to: http://localhost:8000/index.html
     ```

2. **Verify API Connection:**
   - Open browser DevTools (F12)
   - Check Network tab for `/api/data` request
   - Should see `200 OK` status

#### Step 7: Configure AI Integration (Optional)

1. **Get Google Gemini API Key:**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create API key

2. **Update `index.html`:**
   ```javascript
   const API_KEY = 'YOUR_GEMINI_API_KEY';
   ```

### Development Workflow

```mermaid
graph LR
    A[Start] --> B[Load Data to MongoDB]
    B --> C[Start Flask API]
    C --> D[Open Dashboard]
    D --> E[Test Features]
    E --> F{Working?}
    F -->|Yes| G[Deploy]
    F -->|No| H[Debug]
    H --> E
```

---

## 🐳 Docker Deployment

### Dockerfile

Create `Dockerfile` in project root:

```dockerfile
# Use Python 3.9 slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY api.py .
COPY index.html .

# Expose port
EXPOSE 5001

# Set environment variables
ENV FLASK_APP=api.py
ENV FLASK_ENV=production

# Run Flask app
CMD ["python", "api.py"]
```

### Docker Compose

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "5001:5001"
    environment:
      - MONGO_URI=${MONGO_URI}
      - FLASK_ENV=production
    volumes:
      - ./api.py:/app/api.py
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5001/api/data"]
      interval: 30s
      timeout: 10s
      retries: 3

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./index.html:/usr/share/nginx/html/index.html
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - api
    restart: unless-stopped
```

### Docker Deployment Steps

#### Step 1: Create Requirements File

```bash
echo "flask>=2.0.0
flask-cors>=3.0.0
pymongo>=4.0.0" > requirements.txt
```

#### Step 2: Build Docker Image

```bash
docker build -t dep-dashboard-api .
```

#### Step 3: Run Container

```bash
# Set MongoDB URI as environment variable
export MONGO_URI="mongodb+srv://user:pass@cluster.mongodb.net/myDatabase"

# Run container
docker run -d \
  -p 5001:5001 \
  -e MONGO_URI="$MONGO_URI" \
  --name dep-dashboard \
  dep-dashboard-api
```

#### Step 4: Using Docker Compose

```bash
# Create .env file
echo "MONGO_URI=mongodb+srv://user:pass@cluster.mongodb.net/myDatabase" > .env

# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

#### Step 5: Verify Deployment

```bash
# Check API health
curl http://localhost:5001/api/data

# Check container status
docker ps

# View logs
docker logs dep-dashboard
```

### Docker Best Practices

- ✅ Use `.dockerignore` to exclude unnecessary files
- ✅ Use multi-stage builds for smaller images
- ✅ Set non-root user for security
- ✅ Use environment variables for secrets
- ✅ Implement health checks
- ✅ Use Docker volumes for persistent data

---

## 🔧 Troubleshooting Guide

### Common Issues and Solutions

#### 1. **API Connection Error**

**Problem:** Frontend cannot connect to Flask API

**Symptoms:**
- Console error: `Failed to fetch`
- Network tab shows `ERR_CONNECTION_REFUSED`
- Dashboard shows "Error" in metrics

**Solutions:**

```bash
# Check if Flask server is running
ps aux | grep python

# Verify port 5001 is not in use
lsof -i :5001  # macOS/Linux
netstat -ano | findstr :5001  # Windows

# Restart Flask server
python api.py

# Check CORS configuration
# Ensure flask-cors is installed and CORS(app) is called
```

**Debug Steps:**
1. Open browser DevTools → Network tab
2. Check if `/api/data` request is being made
3. Verify API URL in `index.html` matches Flask server URL
4. Test API directly: `curl http://127.0.0.1:5001/api/data`

---

#### 2. **MongoDB Connection Error**

**Problem:** Cannot connect to MongoDB Atlas

**Symptoms:**
- API returns `500 Internal Server Error`
- Error message: `ServerSelectionTimeoutError`
- Flask logs show connection timeout

**Solutions:**

```python
# Verify connection string format
MONGO_CONNECTION_STRING = 'mongodb+srv://username:password@cluster.mongodb.net/myDatabase?retryWrites=true&w=majority'

# Check MongoDB Atlas:
# 1. Whitelist your IP address (Network Access)
# 2. Verify database user credentials
# 3. Check cluster status (should be running)

# Test connection
from pymongo import MongoClient
try:
    client = MongoClient(MONGO_CONNECTION_STRING, serverSelectionTimeoutMS=5000)
    client.server_info()  # Force connection
    print("Connected successfully")
except Exception as e:
    print(f"Connection failed: {e}")
```

**Debug Steps:**
1. Test connection string in MongoDB Compass
2. Check Atlas Network Access → Add current IP
3. Verify database and collection names match
4. Check MongoDB Atlas logs for connection attempts

---

#### 3. **Empty Data or No Results**

**Problem:** API returns empty array `[]`

**Symptoms:**
- Dashboard loads but shows no data
- All metrics show "0" or "-"
- Map is empty

**Solutions:**

```python
# Verify data exists in MongoDB
from pymongo import MongoClient
client = MongoClient(MONGO_CONNECTION_STRING)
db = client['myDatabase']
collection = db['air_quality_traffic']

# Check document count
print(f"Total documents: {collection.count_documents({})}")

# Check sample document
print(collection.find_one())

# Re-run ETL pipeline if data is missing
# Execute Jupyter notebook cells
```

**Debug Steps:**
1. Verify ETL pipeline completed successfully
2. Check MongoDB collection name matches API code
3. Verify CSV files were processed correctly
4. Re-run data loading if necessary

---

#### 4. **CORS Errors**

**Problem:** Browser blocks API requests due to CORS policy

**Symptoms:**
- Console error: `Access to fetch at '...' from origin '...' has been blocked by CORS policy`
- Network tab shows CORS preflight failure

**Solutions:**

```python
# Ensure flask-cors is installed
pip install flask-cors

# In api.py, ensure CORS is enabled
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # Enable for all routes

# Or configure specific origins
CORS(app, resources={r"/api/*": {"origins": "*"}})
```

---

#### 5. **AI/Gemini API Errors**

**Problem:** AI analysis fails or returns errors

**Symptoms:**
- AI Analyst panel shows error messages
- "Invalid API key" or "Rate limit exceeded"
- Analysis requests timeout

**Solutions:**

```javascript
// Verify API key is correct
const API_KEY = 'AIzaSy...';  // Check key format

// Check API quota/limits
// Visit: https://makersuite.google.com/app/apikey

// Implement retry logic (already in code)
// Check network connectivity
// Verify API endpoint URL is correct
```

**Debug Steps:**
1. Test API key in Google AI Studio
2. Check API quota and billing
3. Verify network allows outbound HTTPS
4. Check browser console for detailed error messages

---

#### 6. **Map Not Displaying**

**Problem:** Leaflet map doesn't render

**Symptoms:**
- Map container is blank/gray
- Console errors about Leaflet.js
- Markers not appearing

**Solutions:**

```html
<!-- Verify Leaflet CSS and JS are loaded -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<!-- Check map container has height -->
<div id="map" style="height: 400px;"></div>

<!-- Verify map initialization code runs after DOM load -->
window.onload = function() {
    // Map initialization code
};
```

---

#### 7. **Charts Not Rendering**

**Problem:** Chart.js charts don't display

**Symptoms:**
- Chart canvas is blank
- Console errors about Chart.js
- Charts show but are empty

**Solutions:**

```javascript
// Verify Chart.js is loaded
console.log(typeof Chart);  // Should be "function"

// Check canvas elements exist
const canvas = document.getElementById('zipChart');
console.log(canvas);  // Should not be null

// Ensure data is available before rendering
if (globalRiskData && globalRiskData.length > 0) {
    renderCharts(globalRiskData);
}
```

---

#### 8. **Port Already in Use**

**Problem:** Flask server cannot start on port 5001

**Symptoms:**
- Error: `Address already in use`
- Port 5001 is occupied

**Solutions:**

```bash
# Find process using port 5001
lsof -i :5001  # macOS/Linux
netstat -ano | findstr :5001  # Windows

# Kill process
kill -9 <PID>  # macOS/Linux
taskkill /PID <PID> /F  # Windows

# Or change port in api.py
app.run(port=5002, debug=True)
```

---

### Performance Optimization

#### Slow API Response

```python
# Add connection pooling
from pymongo import MongoClient
from pymongo.pool import PoolOptions

pool_options = PoolOptions(max_pool_size=10)
client = MongoClient(MONGO_CONNECTION_STRING, pool_options=pool_options)

# Add indexes in MongoDB
collection.create_index("Geo Place Name")
collection.create_index("Name")
```

#### Frontend Loading Issues

```javascript
// Implement data caching
let cachedData = null;
let cacheTimestamp = null;
const CACHE_DURATION = 60000; // 1 minute

async function fetchData() {
    if (cachedData && Date.now() - cacheTimestamp < CACHE_DURATION) {
        return cachedData;
    }
    // Fetch fresh data
}
```

---

## 💼 Use Cases & Applications

### Primary Use Cases

#### 1. **Environmental Monitoring & Risk Assessment**

**Scenario:** NYC DEP needs to monitor air quality across all boroughs in real-time.

**Application:**
- Dashboard provides live risk scores for each borough
- Priority queue identifies critical zones requiring immediate attention
- Geospatial map visualizes pollution hotspots
- Enables proactive resource allocation

**Benefits:**
- ✅ Real-time visibility into environmental conditions
- ✅ Data-driven decision making
- ✅ Reduced response time to pollution events

---

#### 2. **Traffic-Pollution Correlation Analysis**

**Scenario:** Understanding the relationship between traffic volume and air quality.

**Application:**
- Combines traffic count data with PM2.5 measurements
- Calculates composite risk scores (60% PM2.5, 40% traffic)
- Identifies high-traffic areas with elevated pollution
- Supports infrastructure planning decisions

**Benefits:**
- ✅ Evidence-based policy making
- ✅ Targeted intervention strategies
- ✅ Resource optimization

---

#### 3. **AI-Powered Predictive Analytics**

**Scenario:** Forecasting pollution spikes before they occur.

**Application:**
- Gemini AI analyzes historical patterns
- Predicts which areas are at highest risk
- Provides confidence levels and preventive recommendations
- Enables proactive measures

**Benefits:**
- ✅ Early warning system
- ✅ Preventive action planning
- ✅ Reduced health impacts

---

#### 4. **Custom Query Interface for Ad-Hoc Analysis**

**Scenario:** DEP analysts need to ask specific questions about the data.

**Application:**
- Natural language query interface
- AI interprets questions and generates insights
- Examples:
  - "What are the top 3 areas with highest PM2.5?"
  - "Which boroughs have the worst traffic-pollution correlation?"
  - "Show me areas where PM2.5 exceeds 15 μg/m³"

**Benefits:**
- ✅ No SQL knowledge required
- ✅ Fast insights for non-technical users
- ✅ Flexible analysis capabilities

---

#### 5. **Emergency Response & Alert System**

**Scenario:** Rapid response to pollution spikes.

**Application:**
- Live alert simulation demonstrates spike detection
- Audio/visual notifications for critical events
- Priority queue automatically updates
- Action recommendations guide response teams

**Benefits:**
- ✅ Immediate notification system
- ✅ Clear action guidelines
- ✅ Improved emergency response

---

### Industry Applications

#### Government & Public Health
- **Air Quality Monitoring**: Real-time tracking of environmental metrics
- **Public Health Alerts**: Early warning for vulnerable populations
- **Policy Development**: Data-driven environmental regulations
- **Resource Allocation**: Optimize inspection and response teams

#### Urban Planning
- **Infrastructure Planning**: Identify areas needing traffic management
- **Zoning Decisions**: Consider environmental factors in development
- **Transportation Optimization**: Reduce pollution through traffic flow improvements

#### Research & Academia
- **Environmental Studies**: Long-term trend analysis
- **Data Science Projects**: Real-world dataset for ML models
- **Geospatial Analysis**: Spatial correlation studies

#### Corporate Sustainability
- **ESG Reporting**: Environmental impact metrics
- **Supply Chain Management**: Route optimization for lower emissions
- **Compliance Monitoring**: Track environmental regulations

---

## 👤 Author

<div align="center">

### **Harshali Kadam**

**Data Engineer | Full Stack Developer | AI Enthusiast**

[![Email](https://img.shields.io/badge/Email-harshalikadam58@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:harshalikadam58@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Harshali_Kadam-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/harshali-kadam/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-FF6B6B?style=for-the-badge&logo=vercel&logoColor=white)](https://harshali-portfolio-two.vercel.app)

---

**📧 Email:** [harshalikadam58@gmail.com](mailto:harshalikadam58@gmail.com)

**💼 LinkedIn:** [https://www.linkedin.com/in/harshali-kadam/](https://www.linkedin.com/in/harshali-kadam/)

**🌐 Portfolio:** [https://harshali-portfolio-two.vercel.app](https://harshali-portfolio-two.vercel.app)

---

### 🚀 **Let's Connect!**

*Open to collaborations, opportunities, and discussions about data engineering, AI, and full-stack development.*

</div>

---

## 📄 License

This project is developed as part of a data engineering course project. All rights reserved.

---

## 🙏 Acknowledgments

- **NYC Open Data** for providing air quality and traffic datasets
- **Google Gemini** for AI-powered analytics capabilities
- **MongoDB Atlas** for cloud database infrastructure
- **Open Source Community** for excellent libraries and tools

---

<div align="center">

**Built with ❤️ by Harshali Kadam**

⭐ *Star this repo if you find it helpful!*

</div>

