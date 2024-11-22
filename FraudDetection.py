# -*- coding: utf-8 -*-
"""Group_7_DSEM_FINAL_PROJECT.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11tNmpsnPOnuDy7QU0TC2r-SeAVXn8ms1
"""

import pandas as pd


file_path = './bank_transactions_data_2.csv'

# Read the CSV file
data = pd.read_csv(file_path)

# Preview the first few rows
print(data.head())

# Check data types and non-null counts
print(data.info())

# Check for missing values
print(data.isnull().sum())

# Statistical summary for numerical columns
print(data.describe())

# Convert TransactionDate and PreviousTransactionDate to datetime
data['TransactionDate'] = pd.to_datetime(data['TransactionDate'])
data['PreviousTransactionDate'] = pd.to_datetime(data['PreviousTransactionDate'])

# Transaction frequency (days since last transaction)
data['DaysSinceLastTransaction'] = (data['TransactionDate'] - data['PreviousTransactionDate']).dt.days

# TransactionAmount to AccountBalance ratio
data['AmountToBalanceRatio'] = data['TransactionAmount'] / data['AccountBalance']

# 1. Transaction Timing
data['TransactionHour'] = data['TransactionDate'].dt.hour  # Hour of the transaction
data['TransactionDayOfWeek'] = data['TransactionDate'].dt.dayofweek  # Day of the week (Monday=0, Sunday=6)
data['IsWeekend'] = data['TransactionDayOfWeek'].apply(lambda x: 1 if x >= 5 else 0)  # Flag for weekend transactions

# 2. Customer Behavior
data['AvgTransactionAmount'] = data.groupby('AccountID')['TransactionAmount'].transform('mean')  # Average transaction amount
data['TransactionCount'] = data.groupby('AccountID')['TransactionID'].transform('count')  # Count of transactions per account

# 3. Device and Location Analysis
data['UniqueDevicesUsed'] = data.groupby('AccountID')['DeviceID'].transform('nunique')  # Unique devices per account
data['UniqueLocations'] = data.groupby('AccountID')['Location'].transform('nunique')  # Unique locations per account

# 4. Account Activity
data['TransactionAmountStdDev'] = data.groupby('AccountID')['TransactionAmount'].transform('std')  # Transaction amount standard deviation
# Note: Uncomment the following line if AccountCreationDate exists in your dataset
# data['DaysSinceAccountCreation'] = (data['TransactionDate'] - data['AccountCreationDate']).dt.days

# 5. Fraud Indicators
data['LargeTransactionFlag'] = (data['TransactionAmount'] > 0.5 * data['AccountBalance']).astype(int)  # Large transaction flag

# 6. Channel Preferences
data['MostUsedChannel'] = data.groupby('AccountID')['Channel'].transform(lambda x: x.mode()[0])  # Most frequently used channel
data['ChannelDiversity'] = data.groupby('AccountID')['Channel'].transform('nunique')  # Count of unique channels used

# 7. Merchant Interactions
data['PreferredMerchant'] = data.groupby('AccountID')['MerchantID'].transform(lambda x: x.mode()[0])  # Preferred merchant
data['UniqueMerchants'] = data.groupby('AccountID')['MerchantID'].transform('nunique')  # Unique merchants per account

# 8. Transaction Frequency and Ratios
data['DaysSinceLastTransaction'] = (data['TransactionDate'] - data['PreviousTransactionDate']).dt.days  # Days since last transaction
data['AmountToBalanceRatio'] = data['TransactionAmount'] / data['AccountBalance']  # Transaction amount to balance ratio

# List all columns in the dataset
print("Columns in the dataset:")
print(data.columns.tolist())

# Preview the dataset with all columns
print("Preview of the dataset:")
print(data.head())

# Total number of values in the dataset
total_values = data.size  # Rows x Columns
print(f"Total number of values in the dataset: {total_values}")

import matplotlib.pyplot as plt

# Histogram for TransactionAmount
plt.hist(data['TransactionAmount'], bins=20, color='blue', alpha=0.7)
plt.title('Transaction Amount Distribution')
plt.xlabel('Transaction Amount')
plt.ylabel('Frequency')
plt.show()

import seaborn as sns

# Boxplot for TransactionAmount by TransactionType
sns.boxplot(data=data, x='TransactionType', y='TransactionAmount')
plt.title('Transaction Amount by Type')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Distribution of original TransactionAmount
plt.figure(figsize=(10, 6))
sns.histplot(data['TransactionAmount'], bins=30, kde=True, color='blue', alpha=0.7)
plt.title('Distribution of Transaction Amount')
plt.xlabel('Transaction Amount')
plt.ylabel('Frequency')
plt.show()

# Scatter plot of Transaction Amount vs. Account Balance
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='AccountBalance', y='TransactionAmount', hue='TransactionType', palette='coolwarm')
plt.title('Transaction Amount vs. Account Balance')
plt.xlabel('Account Balance')
plt.ylabel('Transaction Amount')
plt.show()

# Boxplot of Transaction Amount by Day of the Week
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='TransactionDayOfWeek', y='TransactionAmount', palette='Set2')
plt.title('Transaction Amount by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Transaction Amount')
plt.xticks(ticks=range(7), labels=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
plt.show()

# Boxplot of Transaction Amount by Hour of the Day
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='TransactionHour', y='TransactionAmount', palette='Set1')
plt.title('Transaction Amount by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Transaction Amount')
plt.show()

# Count plot for large transaction flag against account balance
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='LargeTransactionFlag', hue='TransactionType', palette='Blues')
plt.title('Large Transaction Flag vs. Transaction Type')
plt.xlabel('Large Transaction Flag (0: No, 1: Yes)')
plt.ylabel('Frequency')
plt.show()

# Scatter plot of Channel Diversity vs. Average Transaction Amount
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='ChannelDiversity', y='AvgTransactionAmount', hue='TransactionType', palette='viridis')
plt.title('Channel Diversity vs. Average Transaction Amount')
plt.xlabel('Channel Diversity')
plt.ylabel('Average Transaction Amount')
plt.show()

# Scatter plot for Unique Devices Used vs. Number of Transactions
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='UniqueDevicesUsed', y='TransactionCount', hue='TransactionType', palette='plasma')
plt.title('Unique Devices Used vs. Number of Transactions')
plt.xlabel('Unique Devices Used')
plt.ylabel('Number of Transactions')
plt.show()

# Scatter plot for Transaction Amount vs. Days Since Last Transaction
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='DaysSinceLastTransaction', y='TransactionAmount', hue='TransactionType', palette='coolwarm')
plt.title('Transaction Amount vs. Days Since Last Transaction')
plt.xlabel('Days Since Last Transaction')
plt.ylabel('Transaction Amount')
plt.show()

# Count plot for Preferred Merchant
plt.figure(figsize=(12, 6))
sns.countplot(data=data, x='PreferredMerchant', order=data['PreferredMerchant'].value_counts().index)
plt.title('Frequency of Preferred Merchants')
plt.xlabel('Merchant ID')
plt.ylabel('Frequency')
plt.xticks(rotation=90)
plt.show()

# Boxplot of Transaction Frequency by Customer Occupation
plt.figure(figsize=(12, 6))
sns.boxplot(data=data, x='CustomerOccupation', y='TransactionCount', palette='Set3')
plt.title('Transaction Frequency by Customer Occupation')
plt.xlabel('Customer Occupation')
plt.ylabel('Transaction Count')
plt.xticks(rotation=45)
plt.show()

# Remove 'IsWeekend' column from the numerical dataset
numerical_data = data.select_dtypes(include=['float64', 'int64']).drop(columns=['IsWeekend'], errors='ignore')

# Calculate the correlation matrix
correlation_matrix = numerical_data.corr()

# Display the correlation matrix
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Numerical Features (without IsWeekend)')
plt.show()

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

# Derived Features
data['DaysSinceLastTransaction'] = (pd.to_datetime(data['TransactionDate']) -
                                    pd.to_datetime(data['PreviousTransactionDate'])).dt.days
data['AmountToBalanceRatio'] = data['TransactionAmount'] / data['AccountBalance']
data['TransactionHour'] = pd.to_datetime(data['TransactionDate']).dt.hour
data['TransactionDayOfWeek'] = pd.to_datetime(data['TransactionDate']).dt.dayofweek
data['IsWeekend'] = data['TransactionDayOfWeek'].apply(lambda x: 1 if x >= 5 else 0)

# Aggregated Features
data['AvgTransactionAmount'] = data.groupby('AccountID')['TransactionAmount'].transform('mean')
data['TransactionCount'] = data.groupby('AccountID')['TransactionID'].transform('count')
data['UniqueDevicesUsed'] = data.groupby('AccountID')['DeviceID'].transform('nunique')
data['UniqueLocations'] = data.groupby('AccountID')['Location'].transform('nunique')
data['TransactionAmountStdDev'] = data.groupby('AccountID')['TransactionAmount'].transform('std')
data['LargeTransactionFlag'] = (data['TransactionAmount'] > 0.5 * data['AccountBalance']).astype(int)
data['ChannelDiversity'] = data.groupby('AccountID')['Channel'].transform('nunique')
data['UniqueMerchants'] = data.groupby('AccountID')['MerchantID'].transform('nunique')

# Select features for clustering
features = ['TransactionAmount', 'AmountToBalanceRatio', 'DaysSinceLastTransaction',
            'TransactionHour', 'TransactionDayOfWeek', 'IsWeekend',
            'AvgTransactionAmount', 'TransactionCount', 'UniqueDevicesUsed',
            'UniqueLocations', 'TransactionAmountStdDev', 'LargeTransactionFlag',
            'ChannelDiversity', 'UniqueMerchants']

data_features = data[features].fillna(0)  # Handle missing values

# Normalize the features
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_features)

# Fit the K-Means model with the optimal number of clusters
optimal_clusters = 3  # Adjust based on the elbow plot
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
data['Cluster'] = kmeans.fit_predict(data_scaled)

# Add scaled features for visualization (example: scaled TransactionAmount and DaysSinceLastTransaction)
data['ScaledAmount'] = scaler.fit_transform(data[['TransactionAmount']])
data['ScaledAge'] = scaler.fit_transform(data[['DaysSinceLastTransaction']])

# Identify potential fraud based on high AmountToBalanceRatio and unusual cluster assignments
data['PotentialFraud'] = (data['AmountToBalanceRatio'] > 0.8).astype(int)  # Adjust threshold if needed

# Visualize Clusters with Fraud Highlights
plt.figure(figsize=(10, 6))
scatter = plt.scatter(data['ScaledAmount'], data['ScaledAge'],
                       c=data['Cluster'], cmap='viridis', alpha=0.6, label='Clusters')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            s=200, c='red', label='Centroids')
plt.scatter(data.loc[data['PotentialFraud'] == 1, 'ScaledAmount'],
            data.loc[data['PotentialFraud'] == 1, 'ScaledAge'],
            c='black', marker='x', label='Potential Frauds')

plt.title("K-means Clustering with Potential Frauds Highlighted")
plt.xlabel("Scaled Amount")
plt.ylabel("Scaled Age")
plt.legend(loc='best')
plt.colorbar(scatter, label="Cluster ID")
plt.show()
# Print Potential Fraud Transactions
potential_frauds = data[data['PotentialFraud'] == 1]
print(f"Total Number of Potential Frauds: {len(potential_frauds)}")
print("Potential Fraud Transactions:")
print(potential_frauds)

from sklearn.cluster import DBSCAN
import seaborn as sns
import matplotlib.pyplot as plt

# Select relevant features for DBSCAN
dbscan_features = ['TransactionAmount', 'AmountToBalanceRatio', 'DaysSinceLastTransaction',
                   'TransactionHour', 'TransactionDayOfWeek', 'IsWeekend',
                   'AvgTransactionAmount', 'TransactionCount', 'UniqueDevicesUsed',
                   'UniqueLocations', 'TransactionAmountStdDev', 'LargeTransactionFlag',
                   'ChannelDiversity', 'UniqueMerchants']

X_dbscan = data[dbscan_features].fillna(0)  # Handle missing values

# Scale the features for DBSCAN
scaler = StandardScaler()
X_scaled_dbscan = scaler.fit_transform(X_dbscan)

# Apply DBSCAN clustering
dbscan = DBSCAN(eps=0.3, min_samples=5)  # Adjust eps and min_samples based on the data
dbscan_labels = dbscan.fit_predict(X_scaled_dbscan)

# Add DBSCAN cluster labels to the dataset
data['DBSCAN_Cluster'] = dbscan_labels

# Map the cluster labels to descriptive names
label_mapping = {-1: 'Fraud', 0: 'Normal', 1: 'Suspicious Group 1', 2: 'Suspicious Group 2'}
data['DBSCAN_Cluster'] = data['DBSCAN_Cluster'].map(label_mapping)

# Total number of frauds detected
fraud_count_dbscan = len(data[data['DBSCAN_Cluster'] == 'Fraud'])
print(f"Total Number of Potential Frauds detected by DBSCAN: {fraud_count_dbscan}")

# Plotting the results with DBSCAN clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_scaled_dbscan[:, 0], y=X_scaled_dbscan[:, 1],
                hue=data['DBSCAN_Cluster'], palette='coolwarm', s=60)
plt.title('DBSCAN Clustering on Transactions')
plt.xlabel('Scaled Feature 1 (e.g., TransactionAmount)')
plt.ylabel('Scaled Feature 2 (e.g., AmountToBalanceRatio)')
plt.legend(title='Cluster')
plt.show()

from sklearn.ensemble import IsolationForest
import seaborn as sns
import matplotlib.pyplot as plt

# Select relevant features for Isolation Forest
iso_features = ['TransactionAmount', 'AmountToBalanceRatio', 'DaysSinceLastTransaction',
                'TransactionHour', 'TransactionDayOfWeek', 'IsWeekend',
                'AvgTransactionAmount', 'TransactionCount', 'UniqueDevicesUsed',
                'UniqueLocations', 'TransactionAmountStdDev', 'LargeTransactionFlag',
                'ChannelDiversity', 'UniqueMerchants']

X_iso = data[iso_features].fillna(0)  # Handle missing values

# Scale the features for better performance of Isolation Forest
scaler = StandardScaler()
X_scaled_iso = scaler.fit_transform(X_iso)

# Apply Isolation Forest to identify anomalies
iso_forest = IsolationForest(contamination=0.01, random_state=42)  # Set contamination rate to expected fraud rate
outlier_pred = iso_forest.fit_predict(X_scaled_iso)

# Map the results (-1 for outliers, 1 for normal) to descriptive labels
outlier_mapping = {1: 'Normal', -1: 'Potential Fraud'}
data['Outlier_Prediction'] = pd.Series(outlier_pred).map(outlier_mapping)

# Total number of potential frauds
fraud_count = len(data[data['Outlier_Prediction'] == 'Potential Fraud'])
print(f"Total Number of Potential Frauds detected by Isolation Forest: {fraud_count}")

# Plotting the results with outliers highlighted
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_scaled_iso[:, 0], y=X_scaled_iso[:, 1],
                hue=data['Outlier_Prediction'], palette='coolwarm', s=60)
plt.title('Isolation Forest: Outlier Detection on Transactions')
plt.xlabel('Scaled Feature 1 (e.g., TransactionAmount)')
plt.ylabel('Scaled Feature 2 (e.g., AmountToBalanceRatio)')
plt.legend(title='Outlier Prediction')
plt.show()

# Updated list of features that are more relevant to fraud detection
features = ['TransactionAmount', 'AmountToBalanceRatio', 'DaysSinceLastTransaction',
            'TransactionHour', 'TransactionAmountStdDev', 'LargeTransactionFlag',
            'UniqueDevicesUsed', 'UniqueLocations']

# Prepare the data (features and target)
X = data[features].fillna(0)  # Features
y = (data['Outlier_Prediction'] == 'Potential Fraud').astype(int)  # Binary target (1 for fraud, 0 for normal)

# Split data into training and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scale the features for Linear Regression
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize the Linear Regression model
from sklearn.linear_model import LinearRegression
model = LinearRegression()

# Train the model
model.fit(X_train_scaled, y_train)

# Make predictions
y_pred = model.predict(X_test_scaled)

# Evaluate the model
from sklearn.metrics import mean_squared_error, r2_score
print("Linear Regression Model Performance (Refined Features):")
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R-squared:", r2_score(y_test, y_pred))

# Use the refined set of features from before
features = ['TransactionAmount', 'AmountToBalanceRatio', 'DaysSinceLastTransaction',
            'TransactionHour', 'TransactionAmountStdDev', 'LargeTransactionFlag',
            'UniqueDevicesUsed', 'UniqueLocations']

# Prepare the data (features and target)
X = data[features].fillna(0)  # Features
y = (data['Outlier_Prediction'] == 'Potential Fraud').astype(int)  # Binary target (1 for fraud, 0 for normal)

# Split data into training and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scale the features for Logistic Regression
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize the Logistic Regression model
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(random_state=42)

# Train the model
logreg.fit(X_train_scaled, y_train)

# Make predictions
y_pred = logreg.predict(X_test_scaled)

# Evaluate the model
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
print("Logistic Regression Model Performance:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Prepare the data (features and target)
features = ['TransactionAmount', 'AmountToBalanceRatio', 'DaysSinceLastTransaction',
            'TransactionHour', 'TransactionAmountStdDev', 'LargeTransactionFlag',
            'UniqueDevicesUsed', 'UniqueLocations']
X = data[features].fillna(0)  # Features
y = (data['Outlier_Prediction'] == 'Potential Fraud').astype(int)  # Binary target (1 for fraud, 0 for normal)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scale the features for Random Forest (optional, Random Forests can handle unscaled data, but scaling is often better)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize the Random Forest Classifier model
rf_model = RandomForestClassifier(random_state=42)

# Train the model
rf_model.fit(X_train_scaled, y_train)

# Make predictions
y_pred_rf = rf_model.predict(X_test_scaled)

# Evaluate the model
print("Random Forest Classifier Model Performance:")
print("Accuracy:", accuracy_score(y_test, y_pred_rf))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_rf))
print("Classification Report:\n", classification_report(y_test, y_pred_rf))

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Prepare the data (features and target)
features = ['TransactionAmount', 'AmountToBalanceRatio', 'DaysSinceLastTransaction',
            'TransactionHour', 'TransactionAmountStdDev', 'LargeTransactionFlag',
            'UniqueDevicesUsed', 'UniqueLocations']
X = data[features].fillna(0)  # Features
y = (data['Outlier_Prediction'] == 'Potential Fraud').astype(int)  # Binary target (1 for fraud, 0 for normal)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scale the features for SVC
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize the SVC model
svc_model = SVC(random_state=42)

# Train the model
svc_model.fit(X_train_scaled, y_train)

# Make predictions
y_pred_svc = svc_model.predict(X_test_scaled)

# Evaluate the model
print("Support Vector Classifier (SVC) Model Performance:")
print("Accuracy:", accuracy_score(y_test, y_pred_svc))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_svc))
print("Classification Report:\n", classification_report(y_test, y_pred_svc))

import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Prepare the data (features and target)
features = ['TransactionAmount', 'AmountToBalanceRatio', 'DaysSinceLastTransaction',
            'TransactionHour', 'TransactionAmountStdDev', 'LargeTransactionFlag',
            'UniqueDevicesUsed', 'UniqueLocations']
X = data[features].fillna(0)  # Features
y = (data['Outlier_Prediction'] == 'Potential Fraud').astype(int)  # Binary target (1 for fraud, 0 for normal)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scale the features for XGBoost (optional, but helps for gradient-based methods)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize the XGBoost model
xgb_model = xgb.XGBClassifier(random_state=42)

# Train the model
xgb_model.fit(X_train_scaled, y_train)

# Make predictions
y_pred_xgb = xgb_model.predict(X_test_scaled)

# Evaluate the model
print("XGBoost Model Performance:")
print("Accuracy:", accuracy_score(y_test, y_pred_xgb))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_xgb))
print("Classification Report:\n", classification_report(y_test, y_pred_xgb))