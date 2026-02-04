# Loan Eligibility Prediction Web App

A modern, responsive web application that predicts loan eligibility using machine learning. Features a beautiful UI with light/dark mode support and smooth animations.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Files in the Repository](#files-in-the-repository)
- [Setup and Installation](#setup-and-installation)
- [Running Locally](#running-locally)
- [Deployment Guide](#deployment-guide)
- [Model Details](#model-details)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Loan Eligibility Prediction Web App is a machine learning application that determines whether a loan application is likely to be approved based on input features such as applicant income, loan amount, credit history, and more. The prediction model has been trained on historical loan data.

## Features

✨ **Modern UI Design**
- Beautiful gradient background with radial glow effects
- Fully responsive design (mobile, tablet, desktop)
- Smooth animations and transitions
- Professional form layouts

🌙 **Light & Dark Mode**
- Toggle between light and dark themes
- Preference saved in browser
- Smooth transitions

📱 **Responsive Design**
- Mobile-first approach
- Works perfectly on all devices
- Touch-friendly interface

⚡ **Fast Predictions**
- Real-time loan eligibility prediction
- Instant feedback with animated results

## Files in the Repository

- `app.py`: Main Flask application script with prediction logic
- `Loan Eligibility Prediction Model.ipynb`: Jupyter notebook with data preprocessing and model training
- `model.pkl`: Pre-trained machine learning model
- `Dataset/Data.csv`: Training dataset
- `static/style.css`: Modern CSS styling with dark mode support
- `templates/index.html`: Application input form
- `templates/result.html`: Prediction result display page
- `requirements.txt`: Python dependencies

## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning)

### Local Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/loan-eligibility-prediction.git
    cd loan-eligibility-prediction
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Running Locally

1. **Start the Flask development server:**
    ```bash
    python app.py
    ```

2. **Open your browser and navigate to:**
    ```
    http://localhost:5000
    ```

3. **Fill out the form and click "Check Eligibility" to get predictions**

## Deployment Guide

### Option 1: Deploy on Heroku (Easiest)

1. **Install Heroku CLI:**
   - Download from https://devcenter.heroku.com/articles/heroku-cli

2. **Create Heroku Account:**
   - Sign up at https://www.heroku.com

3. **Initialize Git (if not already done):**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

4. **Create Procfile:**
   ```bash
   echo "web: python app.py" > Procfile
   ```

5. **Create requirements.txt (if not exists):**
   ```bash
   pip freeze > requirements.txt
   ```

6. **Deploy to Heroku:**
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   heroku open
   ```

### Option 2: Deploy on PythonAnywhere

1. **Sign up at https://www.pythonanywhere.com**

2. **Upload your project:**
   - Use Web tab to create a new web app
   - Choose Flask and Python version
   - Upload files via file browser

3. **Configure:**
   - Set up your virtual environment
   - Install dependencies: `pip install flask pickle`
   - Configure WSGI file to point to your Flask app

4. **Your app will be live at:**
   ```
   https://yourusername.pythonanywhere.com
   ```

### Option 3: Deploy on Railway

1. **Sign up at https://railway.app**

2. **Connect your GitHub repository:**
   - Push project to GitHub
   - Connect Railway to your GitHub account
   - Select repository to deploy

3. **Configure environment:**
   - Add environment variables if needed
   - Railway auto-detects Flask apps

4. **Deploy:**
   - Railway automatically deploys on push

### Option 4: Deploy on Render

1. **Sign up at https://render.com**

2. **Create new Web Service:**
   - Connect GitHub repository
   - Select Python as runtime
   - Build command: `pip install -r requirements.txt`
   - Start command: `python app.py`

3. **Configure:**
   - Set Port: 5000
   - Deploy and get live URL

### Option 5: Deploy on AWS (Advanced)

1. **Use Elastic Beanstalk:**
   ```bash
   pip install awsebcli-ce
   eb init
   eb create loan-eligibility-env
   eb deploy
   ```

2. **Or use EC2 + Gunicorn:**
   ```bash
   pip install gunicorn
   gunicorn app:app
   ```

### Option 6: Deploy with Docker

1. **Create Dockerfile:**
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   CMD ["python", "app.py"]
   ```

2. **Build and run:**
   ```bash
   docker build -t loan-eligibility .
   docker run -p 5000:5000 loan-eligibility
   ```

3. **Deploy to container services:**
   - Docker Hub
   - AWS ECR
   - Google Container Registry

## Recommended Deployment Platforms

| Platform | Difficulty | Cost | Speed |
|----------|-----------|------|-------|
| Heroku | Easy | Free/Paid | Fast |
| PythonAnywhere | Easy | Free/Paid | Fast |
| Railway | Medium | Free/Paid | Very Fast |
| Render | Medium | Free/Paid | Fast |
| Vercel + Backend | Medium | Free/Paid | Fast |
| AWS | Hard | Pay-as-you-go | Medium |

## Post-Deployment Checklist

- [ ] Test all form fields
- [ ] Verify dark mode works
- [ ] Check mobile responsiveness
- [ ] Test prediction functionality
- [ ] Set up custom domain (if needed)
- [ ] Enable HTTPS
- [ ] Monitor application logs
- [ ] Set up error tracking

## Environment Variables

If deploying, you may want to add:
```
FLASK_ENV=production
DEBUG=False
```

## Model Details

The prediction model uses the following features:
- ApplicantIncome
- CoapplicantIncome
- LoanAmount
- Loan_Amount_Term
- Credit_History
- Gender
- Married
- Education
- Self_Employed
- Property_Area (Rural/Semi-urban/Urban)

Model accuracy and details can be found in the Jupyter notebook.

## Troubleshooting

**Port already in use:**
```bash
python app.py --port 8000
```

**Model file not found:**
- Ensure `model.pkl` is in the project root
- Check file permissions

**Static files not loading:**
- Verify `static/` folder exists
- Check CSS file path in HTML

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## License

This project is licensed under the MIT License - see LICENSE file for details.

4. Run the application:
    ```bash
    python app.py
    ```

## Usage

1. Ensure that the web server is running by executing `python app.py`.
2. Open your web browser and navigate to `http://localhost:5000`.
3. Enter the required loan application details in the form provided.
4. Submit the form to receive the loan eligibility prediction.

## Model Details

The machine learning model used in this project is a [type of model, e.g., Logistic Regression, Random Forest, etc.], trained on a dataset containing various features related to loan applicants. The model was trained using the steps outlined in the `Loan Eligibility Prediction Model.ipynb` notebook.

### Key Features Used in the Model:

- Applicant Income
- Loan Amount
- Credit History
- Property Area
- And others...

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your proposed changes.
