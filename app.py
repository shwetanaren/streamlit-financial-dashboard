import streamlit as st
from multiapp import MultiApp
from pages import home, data_stats, dash, ta # import your application pages here

app = MultiApp()

st.sidebar.header('Navigation')
# Import all your application views here

app.add_app("About", home.app)
# app.add_app("Technical Analysis Indicators", data_stats.app)
app.add_app("Technical Analysis", ta.app)
app.add_app("Sentiment Tracker", dash.app)


# The main app
app.run()

