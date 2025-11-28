# Render Deployment Checklist

## ✅ Pre-Deployment Checklist

### Required Files
- [x] `app.py` - Flask application entry point
- [x] `requirements.txt` - Python dependencies with versions
- [x] `render.yaml` - Render deployment configuration
- [x] `Procfile` - Alternative deployment config
- [x] `.gitignore` - Git ignore rules (allows model.pkl)
- [x] `ml/predict.py` - Prediction module
- [x] `ml/__init__.py` - ML package init
- [x] `frontend/` - Frontend files (HTML, CSS, JS)

### Model File
- [ ] **CRITICAL**: `ml/model.pkl` must exist before deployment
  - Option 1: Train locally and commit: `python ml/train_model.py`
  - Option 2: Train during build (update render.yaml buildCommand)

### Configuration
- [x] `render.yaml` configured with correct start command
- [x] `Procfile` uses PORT environment variable
- [x] Error handling in app.py for missing model
- [x] All paths are relative (works on Render)

### Testing
- [ ] Test locally: `python app.py`
- [ ] Test prediction endpoint with sample data
- [ ] Verify model loads correctly

## 🚀 Deployment Steps

1. **Ensure model.pkl exists** (train if needed)
2. **Commit all files** to your repository
3. **Push to GitHub/GitLab/Bitbucket**
4. **Connect repository to Render**
5. **Deploy and monitor logs**

## ⚠️ Common Issues

- **Model missing**: App will return 503 error on /predict
- **Port binding**: Already handled in render.yaml and Procfile
- **Static files**: Configured correctly in app.py

