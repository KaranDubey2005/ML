# NSCLC Immunotherapy Helper

A machine learning web application that predicts durable clinical benefit from immunotherapy for metastatic Non-Small Cell Lung Cancer (NSCLC) patients using basic clinical markers.

## Problem Statement

Use basic clinical markers to predict durable clinical benefit (1) versus no durable benefit (0) and guide immunotherapy choices for metastatic NSCLC patients.

## Features

- **Web Interface**: Simple, user-friendly form to input patient data
- **ML Prediction**: Random Forest model trained on clinical markers
- **Real-time Recommendations**: Instant probability scores and treatment recommendations

## Clinical Markers Used

- Age
- Sex
- Smoking Status
- PD-L1 expression level
- Tumor Mutational Burden (TMB)
- KRAS mutation status
- EGFR mutation status

## Project Structure

```
.
├── app.py                 # Flask application entry point
├── requirements.txt       # Python dependencies
├── render.yaml           # Render deployment configuration
├── ml/                   # Machine learning module
│   ├── __init__.py
│   ├── predict.py        # Prediction function
│   ├── preprocess.py     # Data preprocessing
│   ├── train_model.py    # Model training script
│   └── model.pkl         # Trained model (generated)
├── frontend/             # Frontend files
│   ├── index.html
│   ├── app.js
│   └── styles.css
└── data/                 # Data directory
    └── processed/        # Processed data (generated)
```

## Setup and Training

### Prerequisites

- Python 3.11+
- pip

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Machine_Learning_Project-main
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Training the Model

1. Place your raw data file as `data.csv` in the project root with the following columns:
   - `patient_age`
   - `patient_gender`
   - `smoking_history`
   - `PD-L1_expression_level`
   - `tumor_mutational_burden`
   - `KRAS_mutation_status`
   - `EGFR_mutation_status`
   - `survival_time_months`
   - `immunotherapy_received`

2. Preprocess the data:
```bash
python ml/preprocess.py
```

3. Train the model:
```bash
python ml/train_model.py
```

This will generate `ml/model.pkl` which is required for predictions.

## Running the Application

### Local Development

```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Production (Gunicorn)

```bash
gunicorn app:app
```

## Deployment on Render

This project is configured for deployment on Render:

1. **Connect your repository** to Render
2. **Create a new Web Service** and select your repository
3. Render will automatically detect the `render.yaml` configuration
4. **Important**: Make sure to include `ml/model.pkl` in your repository or generate it during build

### Build Configuration

The `render.yaml` file configures:
- Python 3.11.0
- Automatic dependency installation
- Gunicorn as the WSGI server

### Model File for Deployment

For deployment, you have two options:

1. **Include the model in the repository** (if it's not too large):
   - Train the model locally
   - Commit `ml/model.pkl` to the repository

2. **Generate during build** (recommended for large models):
   - Add a build script that downloads/generates the model
   - Or use Render's build command to train the model

## API Endpoints

### GET `/`
Returns the main HTML page.

### POST `/predict`
Predicts immunotherapy benefit probability.

**Request Body:**
```json
{
  "age": 65,
  "sex": 1,
  "smoking_status": 1,
  "pd_l1": 50.0,
  "tmb": 10.5,
  "kras_mutated": 0,
  "egfr_mutated": 0
}
```

**Response:**
```json
{
  "probability": 0.75,
  "recommendation": "recommend immunotherapy"
}
```

## Model Details

- **Algorithm**: Random Forest Classifier
- **Features**: 7 clinical markers
- **Target**: Durable clinical benefit (binary classification)
- **Training**: 80/20 train-test split with random_state=42

## License

This project is for educational/research purposes.

## Author

Sachin Chauhan
# ML
