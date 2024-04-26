##prepping and data reading
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import pandas as pd
import statsmodels.api as sm
pio.templates.default = "plotly_white"

data = pd.read_csv("userbehaviour.csv")
print(data.head())

#gaging app user screen time
print(f'Average Screen Time = {data["Average Screen Time"].mean()}')
print(f'Highest Screen Time = {data["Average Screen Time"].max()}')
print(f'Lowest Screen Time = {data["Average Screen Time"].min()}')

##gaging app user total spend time on app
print(f'Average Spend of the Users = {data["Average Spent on App (INR)"].mean()}')
print(f'Highest Spend of the Users = {data["Average Spent on App (INR)"].max()}')
print(f'Lowest Spend of the Users = {data["Average Spent on App (INR)"].min()}')

##relationship btwn spending capacity and screen time of users w/ app & uninstalled app 
figure = px.scatter(data_frame = data, 
                    x="Average Screen Time",
                    y="Average Spent on App (INR)", 
                    size="Average Spent on App (INR)", 
                    color= "Status",
                    title = "Relationship Between Spending Capacity and Screentime",
                    trendline='ols' )
figure.show()