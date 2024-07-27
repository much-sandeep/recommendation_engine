from pytrends.request import TrendReq
import pandas as pd



class RecomendationEngine(): 

    def __init__(self, language = "en-US"): 
        self.trend = TrendReq(hl=language, tz=360)

    def get_trending_topics(self, country): 
        """
        Gets the Trending Topics for the Given Country 
        """
        try:
            data = self.trend.trending_searches(pn=country)
            return data
        except Exception as e:
            print(f"An error occurred: {e}")
            return pd.DataFrame()  





if __name__=="__main__": 
    # Connect to Google
    # tren_obj =GetTrend() 
    # data = tren_obj.get_recommendation(["Python", "java"])
    pytrends = TrendReq()
    data = pytrends.trending_searches(pn='india')


    print(data)