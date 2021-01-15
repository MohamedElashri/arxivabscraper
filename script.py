import arxivabscraper
import pandas as pd

scraper = arxivabscraper.Scraper(category='physics:cond-mat', date_from='2018-05-02',date_until='2020-06-02')

output = scraper.scrape()
cols = ('id','abstract')
df = pd.DataFrame(output,columns=cols)
df.to_csv('df.csv') 
with open('df', 'w') as f: 
f.write('0123456789abcdef')
