import streamlit as st
import pandas as pd
import numpy as np
import requests
from requests.api import options


def app():

    sentiment_option = add_sentimenttracker = st.sidebar.selectbox(
        "Select the sentiment tracker?",
        ( "stocktwits", "wallstreetbets","tweepy")
    )

    if sentiment_option == "stocktwits":
        st.subheader("Results from Stockwits")
        symbol = st.sidebar.text_input("Symbol", value='UBER', max_chars=8)
        pass
        r = requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json")
        
        data = r.json()

        for message in data['messages']:
            st.image(message['user']['avatar_url'])
            st.write(message['user']['username'])
            st.write(message['created_at'])
            st.write(message['body'])
