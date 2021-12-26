import pandas as pd
import plotly.express as px

reading = pd.read_csv("Income-Chart.csv")
plotting = px.line(reading, x = "Year", y = "Per capita income", color = "Country", title = "Per capita income")
plotting.show()