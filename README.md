# 🚨 Fraud Detection Using Machine Learning

## 📄 Project Overview:
This project aims to develop machine learning models to detect fraudulent transactions from a dataset of bank transactions. The dataset contains records of transactions with features such as transaction amount, account balance, transaction hour, and customer behavior. By analyzing these features, we aim to classify transactions as **fraudulent** or **non-fraudulent**.

## 📊 Dataset
- **Name:** Bank Transactions Dataset  
- **Source:** https://www.kaggle.com/datasets/valakhorasani/bank-transaction-dataset-for-fraud-detection  
- **Description:** Contains records of transactions with the following attributes:  
  - 💰 **TransactionAmount:** The amount of the transaction.  
  - 💳 **AccountBalance:** The balance in the user's account at the time of transaction.  
  - 🕒 **TransactionHour:** The time of day when the transaction occurred.  
  - 🗓 **DaysSinceLastTransaction:** The number of days since the user's last transaction.  
  - 🌍 **DeviceID:** The device used for the transaction.  
  - 🌐 **Location:** The geographic location of the transaction.  
  - 💻 **TransactionCount:** The total number of transactions by the account.  
  - 🔒 **Fraudulent Flag (Target Variable):** Whether the transaction is fraudulent (1 for fraud, 0 for normal).

## 🎯 Objective
Develop **machine learning models** to predict fraudulent transactions based on the features provided in the dataset. The goal is to build models that can distinguish between **fraudulent** and **non-fraudulent** transactions.

## 🛠 Workflow

### 1️⃣ Exploratory Data Analysis (EDA)
- 🔄 **Correlation Matrix:**  
  - Positive correlation between **TransactionAmount** and **AccountBalance**.  
  - Negative correlation between **TransactionHour** and **DaysSinceLastTransaction**.
- 📈 **Visualizations:**  
  - Plotted the distribution of **TransactionAmount** to identify potential outliers (fraudulent transactions).

### 2️⃣ Feature Engineering
- **Input Features (X):**  
  - 💰 **TransactionAmount**  
  - 💳 **AccountBalance**  
  - 🕒 **TransactionHour**  
  - 🗓 **DaysSinceLastTransaction**  
  - 🌍 **DeviceID**  
  - 🌐 **Location**  
  - 💻 **TransactionCount**
- **Target Variable (y):**  
  - 🔒 **Fraudulent Flag** (binary variable indicating if a transaction is fraud or not).

### 3️⃣ Model Development
We experimented with multiple models to predict fraud:

- **Linear Regression**: Not suitable for classification tasks but used as a baseline model.
  - 📉 **MSE (Mean Squared Error)**: 0.011
  - 📊 **R² Score**: 0.02 (low performance for fraud detection)

- **Logistic Regression**: The first model applied for binary classification.
  - **Accuracy**: 98.94%
  - **Precision (Fraud)**: 1.00
  - **Recall (Fraud)**: 0.11 (Low recall for fraud detection)

- **Support Vector Classifier (SVC)**: Used for finding non-linear decision boundaries.
  - **Accuracy**: 98.94%
  - **Precision (Fraud)**: 1.00
  - **Recall (Fraud)**: 0.11 (Similar performance to Logistic Regression)

- **Random Forest Classifier**: An ensemble learning method that performed well on imbalanced data.
  - **Accuracy**: 99.34%
  - **Precision (Fraud)**: 0.70
  - **Recall (Fraud)**: 0.78
  - **F1-Score (Fraud)**: 0.74 (Better fraud detection)

- **XGBoost (Extreme Gradient Boosting)**: A highly effective model for imbalanced datasets.
  - **Accuracy**: 99.60%
  - **Precision (Fraud)**: 0.75
  - **Recall (Fraud)**: 1.00 (Perfect recall for fraud detection)
  - **F1-Score (Fraud)**: 0.86

## 🔍 Results and Insights
- **XGBoost** achieved the best performance with **perfect recall** (1.00) for fraud detection and minimal false positives (only 3).
- **Random Forest** also showed good results, with **78% recall** for fraud detection, but **more false positives** compared to XGBoost.
- **Logistic Regression** and **SVC** performed well on normal transactions but had **low recall for fraud** (only 11%).

### **Key Insights:**
- **Imbalanced Dataset**: The fraud class is rare, which makes it challenging to detect fraud. **XGBoost** performed the best due to its ability to handle imbalanced data and complex patterns.
- **Recall vs. Precision**: In fraud detection, **high recall** is crucial, even if it means having a slightly lower precision (which increases false positives).

## 📂 Files Included
- 📘 **FraudDetection.ipynb:** Jupyter notebook for data preprocessing, modeling, and evaluation.  
- 📊 **Report:** Summarizes the project workflow and findings.

## 🚀 Future Work
- **Hyperparameter Tuning**: Further improve model performance by fine-tuning hyperparameters of **XGBoost** and **Random Forest**.
- **Resampling**: Use techniques like **SMOTE** or **undersampling** to balance the dataset and improve fraud detection performance.
- **Real-time Fraud Detection**: Implement the model in a real-time system to detect fraud in live transactions.

## ✨ Author
**Hritik Singh**  
🎓 MS in Information Systems, Northeastern University  
📧 singh.hr@northeastern.edu  
[🔗 LinkedIn](https://www.linkedin.com/in/hritik-singh9919)
