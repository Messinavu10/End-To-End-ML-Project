# 🍷 Wine Quality Predictor - End-to-End ML Project

A comprehensive machine learning project that demonstrates end-to-end ML pipeline development, from data ingestion to model deployment with a cool web interface.

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [ML Pipeline Stages](#ml-pipeline-stages)

## Project Overview

This project is an end-to-end machine learning application that showcases modern ML engineering practices. It demonstrates how to build a complete ML pipeline from raw data to a production-ready web application.

### What it does:
- **Predicts wine quality** based on 11 chemical properties using ElasticNet regression
- **Provides a web interface** for easy model training and predictions
- **Implements MLOps best practices** with modular code structure
- **Tracks experiments** using MLflow for model versioning and comparison

### Key Learning Outcomes:
- Modular code architecture with proper separation of concerns
- Complete ML pipeline implementation (data ingestion → validation → transformation → training → evaluation)
- Web application development with Flask
- Model deployment and serving
- Experiment tracking and model versioning

## Features

### Machine Learning
- **ElasticNet Regression**: Robust model for wine quality prediction
- **Data Validation**: Schema-based validation ensuring data quality
- **Hyperparameter Tuning**: Optimized alpha and l1_ratio parameters
- **Model Evaluation**: Comprehensive metrics (RMSE, MAE, R²)

### Web Application
- **Modern UI**: Beautiful, responsive design with Bootstrap 5
- **Real-time Training**: Live status updates during model training
- **Interactive Predictions**: User-friendly form with validation
- **Quality Assessment**: Visual quality scores with interpretations

### MLOps & Engineering
- **Modular Architecture**: Clean, maintainable code structure
- **Configuration Management**: YAML-based configuration system
- **Logging**: Comprehensive logging throughout the pipeline
- **Error Handling**: Robust error handling and user feedback

## Architecture

```
End-To-End-ML-Project/
├── src/datascience/           # Core ML pipeline modules
│   ├── components/            # Individual pipeline components
│   ├── config/               # Configuration management
│   ├── constants/            # Path constants
│   ├── entity/               # Data classes and entities
│   ├── pipeline/             # Pipeline orchestration
│   └── utils/                # Utility functions
├── config/                   # Configuration files
├── templates/                # Web application templates
├── artifacts/                # Generated artifacts (models, data)
├── research/                 # Jupyter notebooks for experimentation
└── main.py                   # Pipeline execution script
```

## Tech Stack

### Backend & ML
- **Python 3.10+**: Core programming language
- **Scikit-learn**: Machine learning library
- **Pandas & NumPy**: Data manipulation
- **Flask**: Web framework
- **MLflow**: Experiment tracking and model versioning

### Frontend
- **Bootstrap 5**: Responsive UI framework
- **Font Awesome**: Icons
- **JavaScript**: Interactive features

### DevOps & Tools
- **YAML**: Configuration management
- **Joblib**: Model serialization
- **Docker**: Containerization (optional)

## Installation & Setup

### Prerequisites

#### Option 1: Local Development
- Python 3.10 or higher
- pip (Python package installer)
- Git

#### Option 2: Docker (Recommended for easy setup)
- Docker Desktop installed
- Git

### Method 1: Local Setup

#### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/End-To-End-ML-Project.git
cd End-To-End-ML-Project
```

#### Step 2: Create Virtual Environment
```bash
# Create virtual environment & Activate it
conda create -p venv python==3.10

# Activate virtual environment
conda activate venv/
```

#### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 4: Set Environment Variables (Optional)
For MLflow tracking with DagsHub:
```bash
export MLFLOW_TRACKING_URI="https://dagshub.com/your-username/your-repo.mlflow"
export MLFLOW_TRACKING_USERNAME="your-username"
export MLFLOW_TRACKING_PASSWORD="your-token"
```

### Method 2: Docker Setup (Recommended)

#### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/End-To-End-ML-Project.git
cd End-To-End-ML-Project
```

#### Step 2: Build Docker Image
```bash
docker build -t wine-quality-predictor .
```

#### Step 3: Run the Application
```bash
# Run the container
docker run -p 8080:8080 wine-quality-predictor
```

#### Step 4: Access the Application
Open your browser and navigate to: `http://localhost:8080`

### Docker Commands Reference

#### Build and Run
```bash
# Build the image
docker build -t wine-quality-predictor .

# Run the container
docker run -p 8080:8080 wine-quality-predictor

# Run in detached mode (background)
docker run -d -p 8080:8080 wine-quality-predictor

# Run with volume mounting (for persistent artifacts)
docker run -p 8080:8080 -v $(pwd)/artifacts:/app/artifacts wine-quality-predictor
```

#### Container Management
```bash
# List running containers
docker ps

# Stop a container
docker stop <container_id>

# Remove a container
docker rm <container_id>

# View container logs
docker logs <container_id>

# Execute commands in running container
docker exec -it <container_id> /bin/bash
```

#### Docker Compose (Optional)
Create a `docker-compose.yml` file for easier management:

```yaml
version: '3.8'
services:
  wine-predictor:
    build: .
    ports:
      - "8080:8080"
    volumes:
      - ./artifacts:/app/artifacts
    environment:
      - MLFLOW_TRACKING_URI=${MLFLOW_TRACKING_URI}
      - MLFLOW_TRACKING_USERNAME=${MLFLOW_TRACKING_USERNAME}
      - MLFLOW_TRACKING_PASSWORD=${MLFLOW_TRACKING_PASSWORD}
```

Then run:
```bash
docker-compose up -d
```

## 📖 Usage

### Running the Complete Pipeline
```bash
# Execute the entire ML pipeline
python main.py
```

This will run all stages:
1. **Data Ingestion**: Downloads wine quality dataset
2. **Data Validation**: Validates data against schema
3. **Data Transformation**: Splits data into train/test sets
4. **Model Training**: Trains ElasticNet model
5. **Model Evaluation**: Evaluates and logs metrics

### Running the Web Application
```bash
# Start the Flask web server
python app.py
```

Then open your browser and navigate to: `http://localhost:8080`

### Web Application Workflow
1. **Train Model**: Click "Train Model" button to start training
2. **Monitor Progress**: Watch real-time training status updates
3. **Make Predictions**: Fill in wine parameters and get quality predictions
4. **View Results**: See detailed quality assessment with visual indicators

### Example Wine Parameters
```
Fixed Acidity: 7.4
Volatile Acidity: 0.70
Citric Acid: 0.00
Residual Sugar: 1.9
Chlorides: 0.076
Free Sulfur Dioxide: 11.0
Total Sulfur Dioxide: 34.0
Density: 0.9978
pH: 3.51
Sulphates: 0.56
Alcohol: 9.4
```

## Project Structure

```
End-To-End-ML-Project/
├── app.py                    # Flask web application
├── main.py                   # ML pipeline execution
├── requirements.txt          # Python dependencies
├── config/
│   ├── config.yaml          # Main configuration
│   └── schema.yaml          # Data schema
├── params.yaml              # Model hyperparameters
├── src/
│   └── datascience/
│       ├── components/      # Pipeline components
│       │   ├── data_ingestion.py
│       │   ├── data_validation.py
│       │   ├── data_transformation.py
│       │   ├── model_trainer.py
│       │   └── model_evaluation.py
│       ├── pipeline/        # Pipeline orchestration
│       ├── config/          # Configuration management
│       ├── entity/          # Data classes
│       └── utils/           # Utility functions
├── templates/               # Web templates
│   ├── index.html          # Main page
│   └── results.html        # Results page
├── research/               # Jupyter notebooks
└── artifacts/              # Generated files
    ├── data_ingestion/
    ├── data_validation/
    ├── data_transformation/
    ├── model_trainer/
    └── model_evaluation/
```

## ML Pipeline Stages

### 1. Data Ingestion
- Downloads wine quality dataset from GitHub
- Stores data in artifacts directory
- Handles data source management

### 2. Data Validation
- Validates data against predefined schema
- Checks column names and data types
- Generates validation status report

### 3. Data Transformation
- Splits data into training and test sets (75/25)
- Handles data preprocessing
- Saves processed datasets

### 4. Model Training
- Trains ElasticNet regression model
- Uses optimized hyperparameters
- Saves trained model to artifacts

### 5. Model Evaluation
- Evaluates model performance
- Calculates RMSE, MAE, and R² metrics
- Logs experiments to MLflow
- Saves evaluation results

## Model Performance

The ElasticNet model typically achieves:
- **RMSE**: ~0.8 (Good for wine quality scale 3-9)
- **R² Score**: ~0.3-0.4
- **MAE**: ~0.6

Quality Categories:
- **Excellent** (7-10): Premium wines with exceptional characteristics
- **Good** (6-7): Quality wines suitable for most occasions
- **Average** (5-6): Acceptable wines for casual drinking
- **Poor** (3-5): Below-average quality wines

### Web Endpoints

#### GET `/`
- **Description**: Main application page
- **Response**: HTML page with prediction form

#### POST `/train`
- **Description**: Start model training
- **Response**: JSON with training status

#### GET `/training-status`
- **Description**: Get current training status
- **Response**: JSON with training progress

#### POST `/predict`
- **Description**: Make wine quality prediction
- **Parameters**: 11 wine chemical properties
- **Response**: HTML page with prediction results

## Acknowledgments

- Wine Quality dataset from UCI Machine Learning Repository
- MLflow for experiment tracking
- Bootstrap for the beautiful UI components
- The ML community for best practices and inspiration

---