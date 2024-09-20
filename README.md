# Malware Classification using Machine Learning

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-v2.x-orange.svg)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Google Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)

## 📌 Overview

This branch contains a Google Colab notebook to train a machine-learning pipeline for malware classification. 
The model classifies malware samples into binary (malicious/benign), 4-class, and 16-class categories based on memory dump features.

## 🚀 Features

- Data preprocessing and feature selection
- Stacking ensemble with Random Forest, XGBoost, and Extra Trees as base models
- Neural network meta-learner for improved classification
- Support for binary, 4-class, and 16-class classification
- Cross-validation and multiple experiment runs for robust results
- Model saving functionality

## 📊 Dataset

The model is trained on the [Obfuscated-MalMem2022](https://www.unb.ca/cic/datasets/malmem-2022.html) dataset. 
This dataset is in CSV format with the following structure:
- 55 feature columns 
- 'Category': File name containing malware family name and subcategory
- 'Class': Binary class (Benign/Malicious)

Access dataset [here](https://github.com/codexnyctis/104520751_concept4/blob/dev/nur/ML_training/Obfuscated-MalMem2022.csv)

## 🛠️ Usage

1. Open the `stackingEnsemble.ipynb` notebook in Google Colab.
2. Ensure the dataset is accessible (you may need to upload it to your Google Drive or adjust the notebook to load it from GitHub).
3. Run the cells in the notebook sequentially to preprocess the data, train the models, and view the results.

## 📁 Project Structure

```
dev/nur/ML_training/
│
├── stackingEnsemble.ipynb
├── README.md
│
└── Obfuscated-MalMem2022.csv
```

## 🔧 Customisation

You can customise various aspects of the pipeline directly in the notebook:
- Number of features selected
- Number of experiment runs
- Neural network architecture of the meta-learner
- Base models used in the ensemble

Modify the relevant cells in the notebook to implement these customisations.

## 📊 Current Results

Our current model achieves the following performance metrics:

### Binary Classification
- Accuracy: 1.0000
- Precision: 1.0000
- Recall: 0.9999
- F1-score: 1.0000

### 4-Class Classification
- Accuracy: 0.8923
- Precision: 0.8927
- Recall: 0.8923
- F1-score: 0.8919

### 16-Class Classification
- Accuracy: 0.9188
- Precision: 0.9234
- Recall: 0.9188
- F1-score: 0.9183

These results demonstrate excellent performance in binary classification, with near-perfect scores across all metrics. 
The model also shows strong performance in both 4-class and 16-class classifications, with accuracy and other metrics consistently above 0.89.

## 🎯 Target Improvements

To enhance the current model and analysis, we've identified the following key areas for improvement:

1. Model Performance Enhancement:
   - Experiment with different feature combinations and advanced feature engineering
   - Experiment with different architectures for the meta-learner
   - Implement hyperparameter tuning 

2. Addressing Class Imbalance (especially for 4-class and 16-class problems):
   - Implement oversampling techniques like SMOTE for minority classes
   - Experiment with undersampling techniques for majority classes
   - Use class weights in model training to give more importance to minority classes
   - Evaluate the impact of these techniques on model performance across all classification types

3. Additional Results and Visualisations:
   - Generate and analyse confusion matrices for each classification type
   - Create ROC curves and calculate AUC scores, particularly for binary classification
   - Implement precision-recall curves (useful for imbalanced datasets)
   - Develop feature importance plots to identify the most influential features
   - Perform and visualise detailed error analysis to understand misclassification patterns

4. Performance Metrics:
   - Include additional metrics such as ROC AUC for a more comprehensive evaluation
   - Implement k-fold cross-validation to get more robust performance estimates

By focusing on these target improvements, we aim to enhance the model's accuracy, address the challenges posed by class imbalance, and provide more insightful and comprehensive results for analysis.


## 📞 Contact

Project Maintainer - [codexnyctis](https://github.com/codexnyctis)

Project Link: [https://github.com/codexnyctis/104520751_concept4](https://github.com/codexnyctis/104520751_concept4)



