# Deployment Guide for Render

## Prerequisites

Before deploying to Render, you need to ensure the model file exists.

## Option 1: Include Model in Repository (Recommended)

1. **Train the model locally:**
   ```bash
   # If you have data.csv, run:
   python ml/preprocess.py
   python ml/train_model.py
   ```

2. **Commit the model file:**
   ```bash
   git add ml/model.pkl
   git commit -m "Add trained model for deployment"
   git push
   ```

3. **Deploy on Render:**
   - Connect your repository to Render
   - Render will automatically detect `render.yaml`
   - The deployment will work immediately

## Option 2: Train Model During Build

If you prefer not to commit the model file, you can train it during the build process:

1. **Update render.yaml buildCommand:**
   ```yaml
   buildCommand: pip install -r requirements.txt && python ml/preprocess.py && python ml/train_model.py
   ```

2. **Add data.csv to your repository** (or use environment variables/secrets)

## Deployment Steps

1. **Push your code to GitHub/GitLab/Bitbucket**

2. **Create a new Web Service on Render:**
   - Go to https://dashboard.render.com
   - Click "New +" → "Web Service"
   - Connect your repository

3. **Render will auto-detect configuration:**
   - Python environment
   - Build command from `render.yaml`
   - Start command from `render.yaml`

4. **Verify deployment:**
   - Check build logs for any errors
   - Visit your app URL
   - Test the `/predict` endpoint

## Important Notes

- **Model File**: The app requires `ml/model.pkl` to make predictions
- **Port**: Render automatically sets the `PORT` environment variable
- **Static Files**: Frontend files are served from the `frontend/` directory
- **Dependencies**: All Python packages are installed from `requirements.txt`

## Troubleshooting

### Model Not Found Error
- Ensure `ml/model.pkl` exists in your repository
- Or update build command to train the model during build
- Check build logs for model training errors

### Build Fails
- Check Python version compatibility (3.11.0)
- Verify all dependencies in `requirements.txt`
- Check build logs for specific error messages

### App Crashes on Start
- Verify `gunicorn` is in `requirements.txt`
- Check that `app.py` is in the root directory
- Review application logs in Render dashboard

