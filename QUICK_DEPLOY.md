# 🚀 Quick Deploy Commands for Render

## Copy and Paste These Commands in Order:

### 1️⃣ Test Locally First
```powershell
# Install dependencies
pip install -r requirements.txt

# Test the app
python app.py
```
Press `Ctrl+C` to stop the server after testing.

---

### 2️⃣ Train Model (if needed)
```powershell
# Only if you have data.csv file
python ml/preprocess.py
python ml/train_model.py
```

---

### 3️⃣ Prepare Git Repository
```powershell
# Initialize git (if not done)
git init

# Add all files
git add .

# Commit
git commit -m "Ready for Render deployment"

# Add remote (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

### 4️⃣ Deploy on Render

**Option A: Automatic (Using render.yaml)**
1. Go to https://dashboard.render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Render will auto-detect `render.yaml` ✅
5. Click "Create Web Service"

**Option B: Manual Configuration**
If `render.yaml` doesn't work, enter these in Render Dashboard:

**Build Command:**
```
pip install --upgrade pip && pip install -r requirements.txt
```

**Start Command:**
```
gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 120 app:app
```

**Environment Variables:**
- `PYTHON_VERSION` = `3.11.0`
- `FLASK_ENV` = `production`

---

## ✅ Verification Commands

```powershell
# Check if model exists
dir ml\model.pkl

# Check Python version
python --version

# Test imports
python -c "from ml.predict import predict_patient; print('OK')"
```

---

## 📝 One-Line Commands Reference

**Local Test:**
```powershell
python app.py
```

**Install Dependencies:**
```powershell
pip install -r requirements.txt
```

**Git Push:**
```powershell
git add . && git commit -m "Deploy" && git push
```

**Train Model:**
```powershell
python ml/preprocess.py && python ml/train_model.py
```

