import ray
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

@ray.remote
def request_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.select_one("h2#title_area").get_text()

    
    
df = pd.read_csv("data.csv")
ray.init(num_cpus=12)

start = time.time()
titles = [request_url.remote(line[1].url) for line in df.iterrows()]
titles = ray.get(titles)
print(titles)
print("Time taken: ", time.time()-start)