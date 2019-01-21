from bs4 import BeautifulSoup
import requests
import csv
# import sys #for UTF and twitter
# import tweepy, time 
import lxml #to use with BS

existingUrls = []
#for Twitter
# CONSUMER_KEY = ''
# CONSUMER_SECRET = ''
# ACCESS_KEY = ''
# ACCESS_SECRET = ''
# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
# api = tweepy.API(auth)
# reload(sys)
# sys.setdefaultencoding('utf-8')

with open('tenders.csv', 'r') as oldfile:
	tenders = csv.DictReader(oldfile, delimiter='|')
	for row in tenders:
            existingUrls.append(row['url'])

r  = requests.get("https://buyandsell.gc.ca/procurement-data/search/site?&solrsort=dds_publication_date%20desc&f%5B0%5D=ss_publishing_status%3ASDS-SS-005")
data = r.text
soup = BeautifulSoup(data, "lxml")
results = soup.find("ul", class_="search-results").findAll('li', class_="search-result")

for i in results:
    url = i.find("h2").find("a", href=True)
    if url['href'] not in existingUrls:
        with open('tenders.csv', 'a') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter="|")
            csvwriter.writerow([url.text, url['href']])