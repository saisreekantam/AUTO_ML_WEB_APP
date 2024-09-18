AutoML Web App
This project is an AutoML web application built with Streamlit. It allows users to upload datasets, perform data profiling, and automatically build and deploy machine learning models. The app also provides options for data exploration, model selection, and downloading the trained model.

Features
Upload Data: Upload a CSV file to analyze and use for machine learning.
Data Profiling: Automatically generate data profiles, including statistics, visualizations, and data quality reports.
Machine Learning: Automatically build machine learning models using AutoML. Select a target column and let the app find the best model.
Download Model: Download the trained machine learning model for future use.
Tech Stack
Streamlit: For building the web interface.
Pandas: For handling and manipulating the dataset.
Dataprep: For data profiling and cleaning.
PyCaret: For AutoML functionalities (setup, model comparison, and saving models).
How to Run
Clone this repository:

bash
Copy code
git clone https://github.com/yourusername/automl-web-app.git
cd automl-web-app
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy code
streamlit run app.py
Access the app at http://localhost:8501 in your browser.

Usage
1. Upload Data
Navigate to the "UploadData" tab to upload a CSV file.
Once uploaded, the data will be displayed in a table.
2. Data Profiling
In the "Profiling" tab, generate an in-depth data analysis report.
If no data is uploaded, you'll be prompted to upload a file first.
3. Machine Learning
In the "ML" tab, select the target column from the uploaded dataset.
Click "Run Modelling" to start the AutoML process. The best model will be selected based on the dataset.
4. Download Model
Once the model is trained, navigate to the "DownloadModel" tab to download the best-performing model as a .pkl file.
Requirements
Python 3.x
Required Python packages listed in requirements.txt:
streamlit
pandas
dataprep
pycaret
