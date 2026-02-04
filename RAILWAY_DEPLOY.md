# Railway Deployment Guide for Loan Eligibility Predictor

## 🚀 Quick Deployment Steps

### Step 1: Initialize Git (if not already done)
```bash
git init
git add .
git commit -m "Initial commit - Ready for Railway"
```

### Step 2: Push to GitHub
1. Create a new repository on GitHub
2. Add remote and push:
   ```bash
   git remote add origin https://github.com/yourusername/loan-eligibility-prediction.git
   git branch -M main
   git push -u origin main
   ```

### Step 3: Deploy on Railway
1. Go to https://railway.app
2. Click "New Project"
3. Select "Deploy from GitHub"
4. Choose your repository
5. Railway will auto-detect Flask and deploy!

### Step 4: Get Your Live Link
- Railway will show you a URL like: `https://yourapp-production.up.railway.app`
- Share this link with anyone to use your app!

## ✅ What's Included

✓ `requirements.txt` - All dependencies
✓ `Procfile` - Railway configuration
✓ `.gitignore` - Git ignore rules
✓ `model.pkl` - Pre-trained model
✓ `app.py` - Flask application
✓ `templates/` - HTML templates
✓ `static/` - CSS styling

## 🔧 Troubleshooting

### App crashes on Railway?
Check logs: Railway dashboard → Logs tab

### Model not found?
Ensure `model.pkl` is committed to Git:
```bash
git add model.pkl
git commit -m "Add model file"
git push
```

### Slow startup?
Normal! First startup takes 30-60 seconds.

## 📊 Environment Variables (Optional)

Add in Railway dashboard if needed:
- `FLASK_ENV=production`
- `DEBUG=False`

## 🎉 You're Done!

Your app is now live and accessible worldwide!
