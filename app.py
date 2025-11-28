from flask import Flask, request, jsonify
from pathlib import Path
import sys
import os

# Add ml directory to path
base = Path(__file__).resolve().parent
sys.path.append(str(base / "ml"))
from predict import predict_patient

app = Flask(__name__, static_folder=str(base / "frontend"), static_url_path="")

@app.get("/")
def home():
    return app.send_static_file("index.html")

@app.post("/predict")
def run_predict():
    try:
        data = request.get_json(force=True) or {}
        prob = predict_patient(data)
        rec = "recommend immunotherapy" if prob >= 0.5 else "do not recommend immunotherapy"
        return jsonify({"probability": prob, "recommendation": rec})
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 503
    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

