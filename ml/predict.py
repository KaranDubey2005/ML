import pandas as pd
import joblib
from pathlib import Path

model_path = Path(__file__).resolve().parent / "model.pkl"
features = ["age", "sex", "smoking_status", "pd_l1", "tmb", "kras_mutated", "egfr_mutated"]

# Lazy load model to avoid errors at import time
_model = None

def _load_model():
    global _model
    if _model is None:
        if not model_path.exists():
            raise FileNotFoundError(f"model.pkl missing at {model_path}. Please train the model first using ml/train_model.py")
        _model = joblib.load(model_path)
    return _model

def predict_patient(data):
    model = _load_model()
    row = {f: data.get(f, 0) for f in features}
    frame = pd.DataFrame([row])
    proba = model.predict_proba(frame)[0][1]
    return float(proba)

