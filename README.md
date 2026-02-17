# DoS Intrusion Detection System (Machine Learning)

A machine learning driven Intrusion Detection System (IDS) designed to detect Denial of Service (DoS) attacks in network traffic data.  
This project applies data engineering, feature analysis, and supervised learning to distinguish benign network activity from malicious attack patterns.

---

## Project Overview

Denial of Service (DoS) attacks can cripple systems by overwhelming network resources and causing service outages.  
The goal of this project was to build a predictive model capable of identifying DoS attacks in real world network traffic.

Using the **CIC-IDS2017 dataset**, a well-known cybersecurity benchmark, this project analyzes network flow features such as packet size, flow duration, and timing metrics to classify traffic as:

- **Benign**
- **Attack**

The system forms a foundation for real-time intrusion detection and prevention systems (IDS/IPS).

---

## Objectives

- Develop a reproducible ML pipeline for intrusion detection  
- Engineer and select meaningful network flow features  
- Train a high performance classifier for binary attack detection  
- Document engineering decisions using ADR methodology  

---

## Tech Stack

### Languages & Libraries
- Python 3.11  
- Pandas  
- NumPy  
- Scikit-Learn  
- XGBoost  

### Data Engineering
- ETL pipeline design  
- Data cleaning and preprocessing    

### Machine Learning
- Supervised binary classification  
- Feature engineering  
- Recursive feature reduction  
- Standardization (feature scaling)  
- Model evaluation (Accuracy, Precision, Recall, F1-Score)

---

## Dataset

**CIC-IDS2017 (Wednesday subset)**

- ~54,000+ samples  
- 78 numerical flow features  
- Realistic enterprise network traffic simulation  
- Includes both benign traffic and multiple DoS attack types  

Dataset includes features such as:

- Packet length statistics  
- Flow duration   
- Traffic direction metrics  

---

## Data Pipeline

1. **Extraction**
   - Loaded CIC-IDS2017 network flow data into Pandas DataFrames  

2. **Transformation**
   - Cleaned column formatting issues  
   - Removed missing values and low-variance features  
   - Consolidated multiple DoS labels into a single "Attack" class  
   - Standardized numerical features  

3. **Load**
   - stored in Pandas DataFrame
---

## Model Development

### Models Used
- XGBoost Classifier  
- Logistic Regression (baseline comparison)

### Feature Engineering
- Variance-based feature removal  
- Recursive feature reduction (XGBoost)  
- Standard scaling  

### Evaluation Metrics
- Accuracy  
- Precision  
- Recall  
- F1-Score  

---

## Architectural Decisions

This project used **Architectural Decision Records (ADR)** to:

- Justify dataset selection  
- Document preprocessing choices  
- Ensure reproducibility  
- Track modeling decisions  

This mirrors real world engineering documentation practices.

---


## Future Improvements

Potential next steps:

- Real time streaming detection pipeline  
- API deployment (FastAPI/Flask)  
- Dashboard visualization (Streamlit)  
- Cloud deployment (AWS/GCP/Azure)  
- Model monitoring and drift detection  

---


