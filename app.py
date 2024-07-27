import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from script.get_recommend import RecomendationEngine

# Initialize the recommendation engine
recc_engine = RecomendationEngine()

def main():
    st.title('Google Trends Recommendation Engine')

    country_of_interest = st.text_input("Enter the Country of Interest:", "")

    if country_of_interest:
        st.write(f"Fetching trending topics for {country_of_interest}...")

        with st.spinner('Fetching data...'):
            data = recc_engine.get_trending_topics(country_of_interest)

            if not data.empty:
                data.columns = ["Trending Topics"]
                st.write("Trending Topics:")

                st.dataframe(data, width=800) 

            else:
                st.write(f"No data found for {country_of_interest}.")
    else:
        st.write("Please enter a country name.")

if __name__ == "__main__":
    main()
