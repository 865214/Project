import streamlit as st
import pandas as pd 
from statsmodels.tsa.arima.model import ARIMA
import numpy as np 
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from matplotlib import pyplot
from pickle import load

# load the model from disk
yearly_model = load(open('C:/Users/Moin Dalvi/Data_Science/Projects/CO2_Forecast_arima.pkl', 'rb'))

monthly_model = load(open('C:/Users/Moin Dalvi/Data_Science/Projects/CO2_Forecast_arima_monthly.pkl', 'rb'))

st.title("Forecasting $CO_2$ Emission")
st.sidebar.subheader("Select CO2 Emission")
nav = st.sidebar.radio("",["Yearly", "Monthly"])
if nav == "Yearly":
    
    st.sidebar.subheader("Select the Years to Forecast from 2015")
    year = st.sidebar.slider("",2015,2034,step = 1)

    lists = int(year)
    if lists == 2015:
       year=1
    elif lists == 2016:
      year=2
    elif lists == 2017:
       year=3
    elif lists == 2018:
       year=4
    elif lists == 2019:
       year=5
    elif lists == 2020:
       year=6
    elif lists == 2021:
       year = 7
    elif lists == 2022:
       year = 8
    elif lists == 2023:
       year = 9
    elif lists == 2024:
       year = 10
    elif lists == 2025:
       year = 12
    elif lists == 2026:
       year = 12
    elif lists == 2027:
       year = 13
    elif lists == 2028:
       year = 14
    elif lists == 2029:
       year = 15
    elif lists == 2030:
       year = 16
    elif lists == 2031:
       year = 17
    elif lists == 2032:
       year = 18
    elif lists == 2033:
       year = 19
    elif lists == 2034:
       year = 20

    st.sidebar.subheader("To Forecast till the Selected Years\n Please Click on the 'Forecast' Button")
    
    
    pred_yearly = pd.DataFrame()
    pred_yearly['CO2 Yearly Emission'] = yearly_model.forecast(year)


    if st.sidebar.button("Forecast"):
       st.subheader(f"$CO_2$ Emission Forecasted from year 2015" )
       pred_yearly
       fig = plt.figure(figsize=(12,4), dpi=100)
       plt.plot(pred_yearly['CO2 Yearly Emission'], label='Auto regression forecast (ARIMA)')
       plt.title('Forecast for next {} years from 2015'.format(year))
       plt.legend(loc='best')

       st.subheader("Line plot for the Forecasted data")
       st.pyplot(fig)

if nav == "Monthly":
    
    st.sidebar.subheader("Select the Number of Months to Forecast from 2014 February")
    month = st.sidebar.slider("",2,120,step = 1)

    st.sidebar.subheader("To Forecast till the Selected Months\n Please Click on the 'Forecast' Button")
    
    
    pred_monthly = pd.DataFrame()
    pred_monthly['CO2 Monthly'] = monthly_model.forecast(month)


    if st.sidebar.button("Forecast"):
       st.subheader(f"$CO_2$ Emission Forecasted from Feb 2014" )
       pred_monthly
       fig1 = plt.figure(figsize=(12,4), dpi=100)
       plt.plot(pred_monthly['CO2 Monthly'], label='Auto regression forecast (ARIMA)')
       plt.title('Forecast for next {} months from 2014 Feb'.format(month))
       plt.legend(loc='best')

       st.subheader("Line plot for the Forecasted data")
       st.pyplot(fig1)
