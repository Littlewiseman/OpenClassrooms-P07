import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64
import seaborn as sns
import matplotlib.pyplot as plt

st.write("""
# Brice Prediction App 
""")

df = pd.read_csv("C:/Users/BNP Leasing Solution/Documents/Projet Streamlit/data_proba_dashboard.csv")

def user_input_features():

    id_client = st.sidebar.selectbox('ID Client',(df["SK_ID_CURR"]))

    data = {'id_client':[i]} for i in df["SK_ID_CURR"], 
            }

    features = df["SK_ID_CURR"].iloc[0]

    return features

input_df = user_input_features()

features = ['AMT_INCOME_TOTAL', 'AMT_CREDIT', 'AMT_ANNUITY', 'AMT_GOODS_PRICE',

       'AMT_BALANCE',

       'MONTHS_BALANCE',

       'AMT_CREDIT_LIMIT_ACTUAL', 'Forest_PROBA']

df = df[features]

st.subheader('Client Input features')

st.write(df)

