import pickle as pik
import streamlit as st
import numpy as np

'''
# Seoul Bike Data Analysis \n
By https://github.com/Makyona \n
---
Here you can predict the number of bikes rented at a particular hour based on various parameters.\n
Based on data analysed from https://archive.ics.uci.edu/ml/machine-learning-databases/00560/SeoulBikeData.csv\n
---
'''
model = pik.load(open("finalmodel.pkl", "rb"))
# Inputs = Hour, Day, Month, Temperature, Humidity, Wind Speed, Visibility,
# Solar Radiation, Rainfall, Snowfall, Season, Holiday, Functioning Day
Hour = st.slider('Hour : ', max_value = 23, value = 18)
Day = st.select_slider('Day : ', value = 'Monday', options=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
Month = st.select_slider('Month : ', value = 'May', options=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
Temperature = st.slider('Temperature C : ', value = 25.00, min_value = -25.00, max_value = 50.00)
Humidity = st.slider('Humidity % : ', value = 50.00, max_value = 100.00)
WindSpeed = st.slider('Wind Speed m/s : ', value = 5.00, max_value = 10.00)
Visibility = st.slider('Visibilty 10m : ', value = 2000, max_value = 2000, min_value = 10)
SolarRADiation = st.slider('Solar Radiation MJ/m2 : ', value = 2.00, max_value = 4.00)
Rainfall = st.slider('Rainfall mm : ', value = 0.00, max_value = 4.00)
Snowfall = st.slider('Snowfall cm : ', value = 0.00, max_value = 10.00)
Season = st.select_slider('Season : ', value = 'Summer', options = ['Summer', 'Autumn', 'Winter', 'Spring'])
Holiday = st.select_slider('Is it a holiday : ', value = 'No', options = ['Yes', 'No'])
FunctioningDay = st.select_slider('Is it a functioning day : ', value = 'Yes', options = ['Yes', 'No'])
day_num = 1
month_num = 1
func_num = 1
holiday_num = 2
seas_num = 1
seas_dict = {'Summer' : 1, 'Autumn' : 2, 'Winter' : 3, 'Spring' : 4}
day_dict = {'Sunday' : 1, 'Monday' : 2, 'Tuesday' : 3, 'Wednesday' : 4, 'Thursday' : 5, 'Friday' : 6, 'Saturday' : 7}
month_dict = {'January' : 1, 'February' : 2, 'March' : 3, 'April' : 4, 'May' : 5, 'June' : 6, 'July' : 7, 'August' : 8, 'September' : 9, 'October' : 10, 'November' : 11, 'December' : 12}
for keyd in day_dict:
    if keyd == Day:
        day_num = day_dict[keyd]
for keym in month_dict:
    if keym == Month:
        month_num = month_dict[keym]
for keys in seas_dict:
    if keys == Season:
        seas_num = seas_dict[keys]
if FunctioningDay == 'Yes':
    func_num = 1
else:
    func_num = 2
if Holiday == 'Yes':
    holiday_num = 1
else:
    holiday_num = 2
arg = np.array([Hour, Temperature, Humidity, WindSpeed, Visibility, SolarRADiation,
 Rainfall, Snowfall, day_num, month_num, seas_num, holiday_num, func_num])
arg = arg.reshape(1,-1)
'''
---
Estimated Bikes Rented / Needed : \n
'''
st.write(str(int(model.predict(arg)**3)))
'''
---
'''



