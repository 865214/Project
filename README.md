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

















