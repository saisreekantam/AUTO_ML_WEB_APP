# AutoML Web App

This project is an **AutoML web application** built using **Streamlit**. It allows users to upload datasets, perform data profiling, and automatically build and deploy machine learning models. The app provides options for data exploration, model selection, and downloading the trained model.

## Features

- **Upload Data**: Upload a CSV file for analysis and machine learning.
- **Data Profiling**: Automatically generate data profiles, including statistics, visualizations, and data quality reports.
- **Machine Learning**: Automatically build machine learning models using AutoML. Select a target column and let the app find the best model.
- **Download Model**: Download the trained machine learning model for future use.

## Tech Stack

- **Streamlit**: For building the web interface.
- **Pandas**: For handling and manipulating datasets.
- **Dataprep**: For data profiling and cleaning.
- **PyCaret**: For AutoML functionalities such as setup, model comparison, and saving models.

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/saisreekantam/AUTO_ML_WEB_APP.git
   cd automl-web-app
2. pip install -r requirements.txt
3. streamlit run app.py
## Usage

### 1. Upload Data

- Navigate to the **UploadData** tab.
- Upload a CSV file. The data will be displayed as a table.

### 2. Data Profiling

- In the **Profiling** tab, generate an in-depth data analysis report.
- If no data is uploaded, you'll be prompted to upload a file.

### 3. Machine Learning

- In the **ML** tab, select the target column from the uploaded dataset.
- Click **Run Modelling** to start the AutoML process. The app will select the best model based on the dataset.

### 4. Download Model

- After training the model, navigate to the **DownloadModel** tab to download the best-performing model as a `.pkl` file.

## Requirements

- Python 3.x
- Required packages in `requirements.txt`:
  - streamlit
  - pandas
  - dataprep
  - pycaret
