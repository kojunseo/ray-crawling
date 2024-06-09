import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def request_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.select_one("h2#title_area").get_text()

    
    
df = pd.read_csv("data.csv")
# for idx, line in enumerate(df.iterrows()):
#     print(request_url(line[1].url))


start = time.time()
titles = [request_url(line[1].url) for line in df.iterrows()]
print(titles)
print("Time taken: ", time.time()-start)