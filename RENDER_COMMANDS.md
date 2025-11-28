# Complete Render Deployment Commands Guide

## 📋 Render Configuration Files

### Option 1: Using render.yaml (Recommended)

**File: `render.yaml`**
```yaml
services:
  - type: web
    name: nsclc-immunotherapy-ml
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn --bind 0.0.0.0:$PORT app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
```

### Option 2: Using Procfile

**File: `Procfile`**
```
web: gunicorn --bind 0.0.0.0:$PORT app:app
```

---

## 🔧 Build Commands (Choose One)

### Basic Build (if model.pkl already exists in repo)
```bash
pip install -r requirements.txt
```

### Build with Model Training (if you have data.csv)
```bash
pip install -r requirements.txt && python ml/preprocess.py && python ml/train_model.py
```

### Build with Model Training (if data.csv is in data/ directory)
```bash
pip install -r requirements.txt && if [ -f data.csv ]; then python ml/preprocess.py && python ml/train_model.py; fi
```

### Build with Python Version Check
```bash
python --version && pip install -r requirements.txt
```

### Full Build with Dependencies and Model
```bash
pip install --upgrade pip && pip install -r requirements.txt && python ml/preprocess.py && python ml/train_model.py
```

---

## 🚀 Start Commands (Choose One)

### Basic Gunicorn Start
```bash
gunicorn app:app
```

### Gunicorn with Port Binding (Recommended)
```bash
gunicorn --bind 0.0.0.0:$PORT app:app
```

### Gunicorn with Workers (Production)
```bash
gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 4 app:app
```

### Gunicorn with Timeout (for long predictions)
```bash
gunicorn --bind 0.0.0.0:$PORT --timeout 120 app:app
```

### Gunicorn with Logging
```bash
gunicorn --bind 0.0.0.0:$PORT --access-logfile - --error-logfile - app:app
```

### Development Mode (Flask directly)
```bash
python app.py
```

---

## 📝 Updated render.yaml Configurations

### Configuration 1: Basic (Model Already Trained)
```yaml
services:
  - type: web
    name: nsclc-immunotherapy-ml
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn --bind 0.0.0.0:$PORT app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
```

### Configuration 2: With Model Training During Build
```yaml
services:
  - type: web
    name: nsclc-immunotherapy-ml
    env: python
    buildCommand: pip install -r requirements.txt && python ml/preprocess.py && python ml/train_model.py
    startCommand: gunicorn --bind 0.0.0.0:$PORT --workers 2 app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
```

### Configuration 3: Production Ready (with error handling)
```yaml
services:
  - type: web
    name: nsclc-immunotherapy-ml
    env: python
    buildCommand: pip install --upgrade pip && pip install -r requirements.txt
    startCommand: gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 120 --access-logfile - --error-logfile - app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
      - key: FLASK_ENV
        value: production
```

### Configuration 4: With Conditional Model Training
```yaml
services:
  - type: web
    name: nsclc-immunotherapy-ml
    env: python
    buildCommand: |
      pip install -r requirements.txt
      if [ -f data.csv ] && [ ! -f ml/model.pkl ]; then
        python ml/preprocess.py && python ml/train_model.py
      fi
    startCommand: gunicorn --bind 0.0.0.0:$PORT app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
```

---

## 🖥️ Local Testing Commands

### Test Flask App Locally
```bash
python app.py
```

### Test with Gunicorn Locally
```bash
gunicorn --bind 0.0.0.0:5000 app:app
```

### Test with Specific Port
```bash
PORT=5000 gunicorn --bind 0.0.0.0:$PORT app:app
```

### Install Dependencies Locally
```bash
pip install -r requirements.txt
```

### Train Model Locally
```bash
python ml/preprocess.py
python ml/train_model.py
```

---

## 🔍 Verification Commands

### Check Python Version
```bash
python --version
```

### Check Installed Packages
```bash
pip list
```

### Verify Model Exists
```bash
ls -la ml/model.pkl
```

### Test Import
```bash
python -c "from ml.predict import predict_patient; print('Import successful')"
```

### Check App Structure
```bash
ls -la
ls -la ml/
ls -la frontend/
```

---

## 📦 Git Commands for Deployment

### Initial Setup
```bash
git init
git add .
git commit -m "Initial commit - Ready for Render deployment"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

### After Making Changes
```bash
git add .
git commit -m "Update for Render deployment"
git push
```

### Add Model File (if trained locally)
```bash
git add ml/model.pkl
git commit -m "Add trained model"
git push
```

---

## 🎯 Render Dashboard Commands/Steps

### Manual Deployment Steps (if not using render.yaml)

1. **Build Command** (in Render Dashboard):
   ```
   pip install -r requirements.txt
   ```

2. **Start Command** (in Render Dashboard):
   ```
   gunicorn --bind 0.0.0.0:$PORT app:app
   ```

3. **Environment Variables** (in Render Dashboard):
   - `PYTHON_VERSION` = `3.11.0`
   - `FLASK_ENV` = `production` (optional)

---

## 🛠️ Troubleshooting Commands

### Check Build Logs
- View in Render Dashboard → Your Service → Logs

### Test Locally Before Deploying
```bash
# Install dependencies
pip install -r requirements.txt

# Test the app
python app.py

# Test with gunicorn
gunicorn app:app
```

### Verify Requirements
```bash
pip install -r requirements.txt --dry-run
```

### Check for Syntax Errors
```bash
python -m py_compile app.py
python -m py_compile ml/predict.py
```

---

## 📊 Recommended Production Configuration

**Best render.yaml for Production:**
```yaml
services:
  - type: web
    name: nsclc-immunotherapy-ml
    env: python
    buildCommand: pip install --upgrade pip && pip install -r requirements.txt
    startCommand: gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 120 app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
      - key: FLASK_ENV
        value: production
```

**Best Procfile for Production:**
```
web: gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 120 app:app
```

---

## ⚡ Quick Deploy Checklist

1. ✅ `render.yaml` or `Procfile` exists
2. ✅ `requirements.txt` has all dependencies
3. ✅ `ml/model.pkl` exists (or build command trains it)
4. ✅ All files committed to git
5. ✅ Repository connected to Render
6. ✅ Build and start commands configured

---

## 🔗 Render-Specific Notes

- **Port**: Render automatically sets `$PORT` - always use it in start command
- **Build Time**: Build commands run in a fresh environment each time
- **Start Time**: Start command runs after successful build
- **Logs**: Available in Render Dashboard
- **Environment**: Python 3.11.0 (as specified)

