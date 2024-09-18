import streamlit as st
import pandas as pd
import os
import dataprep 


with st.sidebar:
    st.image("https://t3.ftcdn.net/jpg/03/34/91/12/360_F_334911218_UijkFoVixOVSYlPLVMdsrBDTNvDkgEj1.jpg")
    st.title("AutoML")
    choices = st.radio("Navigation",["UploadData","Profiling","ML","DownloadModel"])
    st.info("This application allows you to build  and deploy machine learning models using AutoML.")

if os.path.exists("source.csv"):
    df = pd.read_csv("source.csv", index_col=None)

if choices == "UploadData":
    st.title("Upload Data for modelling")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file, index_col=None)
        df.to_csv("source.csv", index=None)
        st.dataframe(df)

elif choices == "Profiling":
    st.title("Data Profiling")
    if os.path.exists("source.csv"):
        df = pd.read_csv("source.csv", index_col=None)
        pr = dataprep.load_dataset(df)
        st_profile_report(pr)
    else:
        st.error("Please upload a dataset first")
if choice == "ML": 
    chosen_target = st.selectbox('Choose the Target Column', df.columns)
    if st.button('Run Modelling'): 
        setup(df, target=chosen_target, silent=True)
        setup_df = pull()
        st.dataframe(setup_df)
        best_model = compare_models()
        compare_df = pull()
        st.dataframe(compare_df)
        save_model(best_model, 'best_model')
if choice == "DownloadModel": 
    with open('best_model.pkl', 'rb') as f: 
        st.download_button('Download Model', f, file_name="best_model.pkl")
