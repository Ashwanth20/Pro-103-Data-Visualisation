import pandas as pd
import plotly.express as px

reading = pd.read_csv("Covid-Chart.csv")
plotting = px.bar(reading, x = "date", y = "cases", color = "country", title = "Data For Covid Cases")
plotting.show()