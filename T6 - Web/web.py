import streamlit as st

# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df_all = pd.read_csv("city_day.csv")
df_delhi = df_all.loc[df_all["City"] == "Delhi"].copy()
df_delhi = df_delhi[["Date", "AQI"]]
df_delhi["Date"] = pd.to_datetime(df_delhi["Date"])
df = df_delhi.set_index("Date")


st.title("My first app")
st.write("Here's our first attempt at using data to create a table:")


st.write(df)
st.line_chart(df)

df2 = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})


option = st.sidebar.selectbox("Which number do you like best?", df2["first column"])
"You selected:", option

