# Peace of Mind: AI-Powered Malware Detection System

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68.0+-00a393.svg)
![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D)


## 🛡️ Overview

Peace of Mind is a malware detection system that combines machine-learning techniques with a user-friendly web interface. 
Our goal is to help detect various types of malware, including trojans, spyware, and ransomware while raising the user's awareness.

## 🎨 Visual Preview

Check out our user interface design on Figma:
[Peace of Mind UI Design](https://www.figma.com/design/RBPSCaUT0Ypx9OuqdGu8kq/detection-system?node-id=0-1&t=kiWQCunuuD8sQN6W-1)

This link provides a visual representation of our user and admin interfaces.

## 🚀 Features

### User Features
- Account registration and login
- Upload .csv files containing dump information for analysis
- Multiple classification levels: binary, 4-class, and 16-class
- View latest 10 scans with file name, status, and date
- Interactive pie chart visualizing all scan results
- Summary statistics: timing of last scan, total scans, clean files, and detected malware
- Bar chart showing malware family distribution
- Detailed information about specific malware families
- Download template CSV file for proper formatting

### Admin Features
- Secure admin login
- View user activity across all users
- Monitor detection alerts sorted by urgency
- Update machine learning model
- Update dataset for improved detection
- Analyze data insights and model performance based on updated model and dataset


## 💻 Tech Stack and Architecture

### Frontend
- **Framework**: Vue.js
- **Visualisation**: Plotly

### Backend
- **API Framework**: FastAPI
- **Machine Learning**:
  - scikit-learn (for model performance analysis)
  - pandas (for dataset insights)
  - Base Learners: Random Forest, XGBoost, Extra Trees Classifier
  - Meta Learner: Neural Network

### Storage
- **User Data/Results**: SQLite 
- **Models/Datasets**: MinIO or free-tier S3 bucket

### Authentication
Handled between Frontend and FastAPI

## 🏗️ Architecture Overview

1. **Frontend**: Vue.js based user interface with Plotly for visualisations.
2. **Backend**: FastAPI server handling requests, file uploads, and serving data.
3. **Machine Learning Pipeline**: Processes data for malware detection and analysis.
4. **Storage**: 
   - SQLite for user data and results
   - MinIO/S3 for storing models and datasets

The FastAPI backend validates files/data before saving and provides data to the frontend. 
It also manages the interaction between the user interface and the machine learning components.

## 🛠️ Installation

1. Clone the repository:
   ```
   git clone https://github.com/codexnyctis/104520751_concept4.git
   cd 104520751_concept4
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages: (will be added after the project is complete)
   ```
   pip install -r requirements.txt
   ```

4. Set up MinIO or configure S3 bucket (will be added after the project is complete)

5. Initialise the SQLite database (will be added after the project is complete)

6. Start the FastAPI server:
   ```
   uvicorn main:app --reload
   ```

7. In a new terminal, set up and run the Vue.js frontend: (will be added after the project is complete)
   ```
   cd (front end location will be added)
   npm install
   npm run serve
   ```

## 📊 Usage

### For Users
1. Register for an account on the Peace of Mind platform.
2. Log in to your dashboard.
3. Download the template CSV file for proper formatting.
4. Prepare your dump information in the CSV format.
5. Upload the CSV file for scanning and analysis.
6. View the scan results, including:
   - Latest scans table
   - Pie chart of overall scan distribution
   - Summary statistics
   - Malware family distribution bar chart
   - Detailed information on detected malware families

### For Administrators
1. Access the admin dashboard using provided credentials.
2. Monitor overall user activity and system performance.
3. View and manage detection alerts, sorted by urgency.
4. Update the machine learning model as needed.
5. Update the dataset to improve detection capabilities.
6. Analyse data insights and model performance metrics.

## 🧠 Machine Learning Model

Our core ML model uses a stacking ensemble approach:
- Base models: Random Forest, XGBoost, Extra Trees
- Meta-learner: Neural Network
- Supports binary, 4-class, and 16-class malware classification

For more details on the ML pipeline, refer to `dev/nur/ML_training/README.md`.

## 🤝 Team
Xiang Li
Mafty Huang
Ryan Lo
Allen Huang
Nur Sarikaya

## 📞 Contact
[Nur Sarikaya](mailto:104520751@student.swin.edu.au)

Project Link: [https://github.com/codexnyctis/104520751_concept4](https://github.com/codexnyctis/104520751_concept4)

---

Stay safe, stay secure. 
