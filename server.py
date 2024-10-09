from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import numpy as np
import joblib
import tensorflow as tf
import json
import os
import traceback
import matplotlib
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
CORS(app)


# Classification Components
def load_model_components(model_path):
    components = {}
    required_files = [
        "base_model_0.joblib", "base_model_1.joblib", "base_model_2.joblib",
        "meta_learner.keras", "le_16class.joblib", "scaler.joblib",
        "feature_selector.joblib", "variance_selector.joblib", "selected_features.json"
    ]

    for file in required_files:
        file_path = os.path.join(model_path, file)
        if file.endswith('.json'):
            with open(file_path, 'r') as f:
                components[file[:-5]] = json.load(f)
        elif file.endswith('.keras'):
            components[file[:-6]] = tf.keras.models.load_model(file_path)
        else:
            components[file[:-7]] = joblib.load(file_path)

    return components

model_components = load_model_components("public/saved_model_16class")

@app.route('/classify', methods=['POST'])
def classify():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file and file.filename.endswith('.csv'):
        # Save the file temporarily
        temp_dir = 'temp'
        os.makedirs(temp_dir, exist_ok=True)
        temp_path = os.path.join(temp_dir, file.filename)
        file.save(temp_path)

        try:
            # Read the CSV file
            df = pd.read_csv(temp_path)
            
            if df.shape[1] != 55:
                return jsonify({'error': f'Expected 55 features, but got {df.shape[1]}'})

            df = df.apply(pd.to_numeric, errors='coerce')
            df = df.fillna(0)

            X = df.values

            X_var = model_components['variance_selector'].transform(X)
            X_selected = model_components['feature_selector'].transform(X_var)
            X_scaled = model_components['scaler'].transform(X_selected)

            base_predictions = []
            for i in range(3):
                base_predictions.append(model_components[f'base_model_{i}'].predict_proba(X_scaled))
            
            meta_features = np.hstack(base_predictions)
            final_predictions = model_components['meta_learner'].predict(meta_features)
            predicted_classes = np.argmax(final_predictions, axis=1)
            
            predicted_labels = model_components['le_16class'].inverse_transform(predicted_classes)
            
            results = []
            for label, confidence in zip(predicted_labels, np.max(final_predictions, axis=1)):
                results.append({
                    'Predicted Class': label,
                    'Confidence': float(confidence)
                })
            
            # Calculate distribution for pie chart
            label_counts = pd.Series(predicted_labels).value_counts()
            pie_data = [{'name': label, 'value': int(count)} for label, count in label_counts.items()]

            return jsonify({
                'classification_results': results,
                'pie_chart_data': pie_data
            })
        
        except Exception as e:
            return jsonify({'error': f'Error processing file: {str(e)}'})
        
        finally:
            # Remove the temporary file
            if os.path.exists(temp_path):
                os.remove(temp_path)
    
    return jsonify({'error': 'Invalid file format'})

@app.route('/api/tips', methods=['GET'])
def get_tips():
    tips = [
        "Use a password manager to create and store strong, unique passwords for each of your accounts; it's like having a personal vault for your digital life! This protects you from password reuse and enhances security. Popular options include LastPass or Bitwarden—just remember to use a strong master password.",
        
        "Set up two-factor authentication (2FA) everywhere you can; it’s like putting a second lock on your front door for extra security. 2FA adds an additional layer of protection, requiring a code sent to your phone or email. Most major platforms offer this feature in their security settings.",
        
        "Keep your software and operating systems up to date; this is your first line of defense against cyber attacks! Updates often include security patches for vulnerabilities. Enable automatic updates in your device settings to ensure you're always protected.",
        
        "Think before you click! Always hover over links to see where they lead and be cautious of unexpected email attachments. This helps you avoid phishing scams. If you receive a suspicious email, verify the sender before opening anything or clicking links.",
        
        "Install reputable antivirus software and ensure it runs regular scans; think of it as a shield against digital intruders. Good antivirus programs can detect malware and remove it before it causes harm. Set your software to perform regular scans and updates automatically.",
        
        "Backup your data regularly to both local and cloud solutions; don’t wait for a disaster to realize how precious your data is! Backing up helps you recover your files in case of loss or theft. Use services like Google Drive or Dropbox and an external hard drive for redundancy.",
        
        "Be aware of phishing attempts; if something looks off, it probably is. Verify before you trust! Check the email address and look for spelling errors or suspicious language. If in doubt, contact the sender through official channels to confirm.",
        
        "When using public Wi-Fi, protect your connection with a VPN; it’s like using a secure tunnel for your online activities. A VPN encrypts your internet connection, making it harder for others to intercept your data. Consider using services like NordVPN or ExpressVPN for added security.",
        
        "Avoid conducting sensitive transactions on public computers; keep your financial information safe by using your own devices. Public computers can have malware or be monitored. If you must use one, ensure it’s a trusted device and always log out after use.",
        
        "Regularly check your accounts for suspicious activity; being proactive can help you catch issues before they escalate. Set aside time each month to review your bank statements and online accounts. Report any unauthorized transactions immediately.",
        
        "Stay informed about common cyber threats; knowledge is power! Share what you learn with friends to keep everyone safe. Follow reputable cybersecurity blogs or news sites to stay updated on emerging threats and prevention techniques.",
        
        "Practice digital spring cleaning: regularly delete old accounts and apps you no longer use to reduce your digital footprint. Old accounts can be a security risk if they’re not monitored. Go through your accounts every few months and close any that are unnecessary.",
        
        "Be mindful of what you share online; adjust your privacy settings to protect your personal information from prying eyes. Limiting personal information can help prevent identity theft. Review your social media privacy settings and limit the visibility of your posts.",
        
        "Know how to identify secure websites (look for HTTPS in the URL) before entering any personal information; it's your online safety net! This ensures that your data is encrypted during transmission. Always check for the padlock icon in the address bar.",
        
        "Remember, cybersecurity is a community effort! Share tips and tricks with friends and family to create a safer online environment for everyone. Encourage open discussions about online safety and share resources to help others stay informed."
    ]
    return jsonify(tips)



@app.route('/api/scan_log', methods=['GET'])
def get_scan_log():
    # This is a mock implementation. You'd fetch this from a database.
    mock_log = [
        {"filename": "system_dump_1.bin", "status": "Clean", "date": "2024-05-14"},
        {"filename": "memory_snapshot.dmp", "status": "Trojan Horse Detected", "date": "2024-05-10"},
        {"filename": "user_data.bin", "status": "Clean", "date": "2024-05-08"},
        {"filename": "network_traffic.pcap", "status": "Potential Malware", "date": "2024-05-05"},
        {"filename": "registry_backup.reg", "status": "Clean", "date": "2024-05-01"}
    ]
    return jsonify(mock_log)


if __name__ == '__main__':
    app.run(debug=True)