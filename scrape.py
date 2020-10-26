import requests as re
from bs4 import BeautifulSoup
import pandas as pd
import lxml
import sqlite3 as db
import time


url = 'https://www2.montgomerycountymd.gov/mcgportalapps/ElectionLocation.aspx?EarlyVoting=1&flag=1'
r = re.get(url)
soup = BeautifulSoup(r.content, 'lxml')

table = soup.find('table')
df = pd.read_html(str(table))[0]
df['timestamp'] = time.time()
#print(df)

con = db.connect('scrape_db.db')

df.to_sql(name='scrape',con=con , if_exists = 'append')

print('success')