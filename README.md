# Project
Forecasting Air Quality for CO2 Emission
# Introduction
There is wide consensus among scientists and policymakers that global warming as defined by the Intergovernmental Panel on Climate Change (IPCC) should be pegged at 1.5 Celsius above the pre-industrial level of warming in order to maintain environmental sustainability . The threats and risks of climate change have been evident in the form of various extreme climate events, such as tsunamis, glacier melting, rising sea levels, and heating up of the atmospheric temperature. Emissions of greenhouse gases, such as carbon dioxide (CO2) are the main cause of global warming.

In this Project for Time Series Analysis and Forecasting 
Each step taken like EDA, Feature Engineering, Model Building,  Model Evaluation and Prediction table, and Deployment. Explaining which model to select on basis of metrics like RMSE, MAPE and MAE value for each model. Finally explaining which model we will use for Forecasting.

Better accuracy in short-term forecasting is required for intermediate planning for the target to reduce CO2 emissions. High stake climate change conventions need accurate predictions of the future emission growth path of the participating organization to make informed decisions. Exponential techniques, Linear statistical modeling and Autoregressive models are used to forecast the emissions and the best model will be selected on these basis
1.) Minimum error 
2.) Low bias and low variance trade off

# DataSet Detail
![image](https://user-images.githubusercontent.com/101926069/185866026-c0ed5021-c01f-49a7-82e8-6df5d51cdc6c.png)
![image](https://user-images.githubusercontent.com/101926069/185866083-737be3d8-1918-4190-bb6d-694dc3516a23.png)
![image](https://user-images.githubusercontent.com/101926069/185866137-1640ce6c-fdc2-4b64-ad15-8af77b98cd18.png)

# Outlier Detection
![image](https://user-images.githubusercontent.com/101926069/185869996-f8c5445a-2033-4f22-b72c-19a15e07e16d.png) ![image](https://user-images.githubusercontent.com/101926069/185870059-4bf7f339-c31f-4336-aa11-4c75b9643437.png)
![image](https://user-images.githubusercontent.com/101926069/185870119-12b50c77-d2ad-4007-8482-d0f481dfddf4.png)
# Observation:There are no outliers above the positive upper extreme whisker.There are no outliers below the negative side of the lower whisker.The data looks right skewed which means there are extreme values that do not follow the regular trend of the data

# Data visualization
![image](https://user-images.githubusercontent.com/101926069/185870450-f883874d-9f3f-4bac-b747-a1c6b903efba.png)
# Observation: As we can observe that approximately after ‘1845’ there is a increase in the amount of ‘CO2’ Emission and at ‘1979’ it was at its peak.There has been significant increase in the amount of ‘CO2’ emission after ‘1870’.With increasing time the amount of emission of ‘CO2’ is also increasing. The lowest ‘CO2’ emission  recorded was ‘0.00175’ on ‘1845’The highest ‘CO2’ that was recorded ‘18.2’ on ‘1979’We can see there was an plateau in ‘CO2’ Emission  from ‘1800’ to ‘1860’ not much of a variance, mostly constant

# Data Visualization : Lag plot (Yearly):
![image](https://user-images.githubusercontent.com/101926069/185874195-3d0cd511-2856-42e6-bfab-3b977239bd5f.png)
# Observation: Our data is linear mostly linear and it shows positive autocorrelation with the previous lag values and it has an underlying structure of and autoregressive model.

# Correlation of the DataSet
![image](https://user-images.githubusercontent.com/101926069/185874496-d7247dcc-8a7b-4f29-b7d3-3082c1891565.png)
![image](https://user-images.githubusercontent.com/101926069/185874571-19dac7dc-5f4c-43e7-b901-55f2ab1342fa.png)
![image](https://user-images.githubusercontent.com/101926069/185874642-01645331-c141-4dd6-bff8-3375c28c55ff.png)
# Observation:There is a positive linear correlation between the independent feature ‘Year’ and the dependent feature ‘CO2’.

# Sampling Yearly into Monthly time series
## Interpolation method
### Using ‘linear’:  You draw a straight line joining the next and previous points of the missing values in the data.
![image](https://user-images.githubusercontent.com/101926069/185875252-953fe6eb-ab39-4b45-9d10-09b5928a4296.png) ![image](https://user-images.githubusercontent.com/101926069/185875343-5f1ceab2-4cf5-4770-a0c7-3c73f8cb390a.png)

# Data Visualization: Lag plot(Monthly)
![image](https://user-images.githubusercontent.com/101926069/185875629-dccfb610-447c-42d6-b9c3-3f9fa9c3f4f9.png)
# Observation: Our data shows positive linear autocorrelation with the previous lag values (previous months)

# Time series decomposition plot
![image](https://user-images.githubusercontent.com/101926069/185876228-d41ec5ee-e5eb-4823-93d4-044108ad2c3e.png)
# Observation:-1.Observed - Actual data (2) Trend - Increasing trend. (3) Seasonal- Does not Varies with the mean 0.No seasonality found. (4) Residual - It is the noise pattern of the time series data for each year, which was not captured by the two components - Trend and Seasonality. Residual is the left over after decomposition of the two major components (Trend and Seasonality)

# Feature Engineering:Feature Extraction
## Feature Extraction for Visualization:
![image](https://user-images.githubusercontent.com/101926069/185877586-a4f09c5e-cf14-4fb3-9ef4-dc8df4987933.png)
## Data Pre-processing for Model Driven Techniques:
![image](https://user-images.githubusercontent.com/101926069/185877761-691da6bb-62cd-4d82-8689-2c50d0df4da5.png)

# Data visualization
![image](https://user-images.githubusercontent.com/101926069/185878007-2785e068-ac52-43ef-a5ff-b6d16a399987.png)
# Observation: As we can observe there is Weekly seasonality in our time series data analysis.Every 23rd week of every Year we can see a spike in CO2 emission in our time series. It does not have Quarterly or Monthly seasonality  through out the years. 
![image](https://user-images.githubusercontent.com/101926069/185878271-69f51d94-06ec-4fe8-b0e9-bf3d368410cb.png)
# Observation: In daily analysis of  𝐶𝑂2  emission we are getting a constant variation among all days throughout the Years.Hence, we can see there is no Daily seasonality or pattern in CO2 emission
![image](https://user-images.githubusercontent.com/101926069/185878464-f75ceed8-1b13-485c-8cc5-de2b3aaef735.png)
![image](https://user-images.githubusercontent.com/101926069/185878510-816d1e6f-18ee-441a-b2b1-12395d2f6573.png)
![image](https://user-images.githubusercontent.com/101926069/185878590-b4bbe2ec-9f0d-4aa5-84df-b52059aa2077.png)

# Splitting the data into train test split
No random partition That’s because the order sequence of the time series should be intact in order to use it for forecasting.
Leaving Test Data with 20 Years of Time Series.We are going to forecast for the last 20 years. that is from 1994 to 2014.
![image](https://user-images.githubusercontent.com/101926069/185878963-69b8a03a-6cb4-4692-bdb6-a68787f73041.png)





















