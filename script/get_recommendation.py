import os 
import sys  


parent_dir = os.path.abspath(os.path.join(os.getcwd(), '.'))
sys.path.append(parent_dir)
print(parent_dir)
from scraper import GoogleTrendsScraper 
from config import CHROMEDRIVER_PATH


gts = GoogleTrendsScraper(sleep=5, path_driver=CHROMEDRIVER_PATH, headless=True)
data = gts.get_trends('movies', '2018-07-02', '2019-04-02', 'US')
print(type(data))
print(data)
del gts