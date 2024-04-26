##prepping and data reading
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import pandas as pd
pio.templates.default = "plotly_white"

data = pd.read_csv("userbehaviour.csv")
print(data.head())