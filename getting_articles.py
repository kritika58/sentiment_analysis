import requests
import json
from newspaper import Article
import csv



url = "https://api.gdeltproject.org/api/v2/doc/doc?query=domain:aljazeera.com&sourcelang:english&maxrecords=250&format=json&startdatetime=20180607000000&enddatetime=20180611000000"


#get page
response = requests.get("https://api.gdeltproject.org/api/v2/doc/doc?query=domain:aljazeera.com&sourcelang:english&maxrecords=250&format=json&startdatetime=20180610000000&enddatetime=20180611000000")
data = response.json()


articles = data['articles']


#for i in articles:
i = articles[0]
link = i['url']
#    print(link)
article1=Article(link)
article1.download()
article1.parse()
print(article1.text)
#    article1.nlp()
#    print(article1.keywords)
    