from newsapi import NewsApiClient
from datetime import date, timedelta
from requests import get
import csv

# NewsAPI initialization
newsapikey = open("api_key.txt").read()
newsapi = NewsApiClient(api_key=newsapikey)

# Load the wordlists into arrays
positive_list = open("positive.txt").read().splitlines()
negative_list = open("negative.txt").read().splitlines()

# Get yesterday's date in the appropriate 
day = str(date.today() - timedelta(1))

# Cycle through each page of results from NewsAPI
# (since we only get 100 results per page)
all_articles = []
page = 1
while True:
	tmp_articles = newsapi.get_everything(
		q='bitcoin',
		from_parameter=day,
		to=day,
		language='en',
		sort_by='relevancy',
		page_size=100,
		page=page)['articles']
	page += 1
	all_articles.extend(tmp_articles)
	# If our request returns no articles, end the search
	if len(tmp_articles) == 0:
		break

# Calculate the sentiment from the article titles
articles = []
t_positive = 0
t_negative = 0
t_neutral = 0
for article in all_articles:
	title = article['title']
	# Remove all non-alphanumeric characters from the article and split it into an array of words
	try:
		exploded_title = ''.join([i for i in title if i.isalpha() or i==" " or i=="'"]).lower().split()
	except:
		exploded_title = [""]
	
	positive = 0
	negative = 0

	# Total all the positive and negative words
	for i in exploded_title:
		if (i in positive_list):
			positive += 1
		if (i in negative_list):
			negative += 1
	# Find the net sentiment of the article
	net = positive - negative
	if net > 0:
		t_positive += 1
	if net < 0:
		t_negative += 1
	if net == 0:
		t_neutral += 1
	
	# Create a dictionary of the results
	articles.append(dict([("title", title), ("exploded_title", exploded_title), ("positive", positive), ("negative", negative), ("net", net)]))

n = len(articles)

# Get Bitcoin's closing price yesterday
price = get("https://api.coindesk.com/v1/bpi/historical/close.json").json()["bpi"][day]

# Write the results to disk
with open("data.csv", "a") as f:
	f.write(
		day + "," +
		str(t_positive) + "," +
		str(t_negative) + "," +
		str(t_neutral) + "," +
		str(n) + "," +
		str(t_positive - t_negative) + "," +
		str(t_positive / n) + "," + 
		str(t_negative / n) + "," + 
		str((t_positive + t_negative) / n) + "," +
		str(price) +
		"\n")

### Print the results (remove this if automating) ###
# Positive articles
print("     +: " + str(t_positive))

# Negative articles
print("     -: " + str(t_negative))

# Neutral or inconclusive articles
print("     ~: " + str(t_neutral))

# Number of total articles
print("     n: " + str(n))

# Number of API requests
print("    tx: " + str(page-1))

# Overall sentiment
print(" sent : " + str(t_positive - t_negative))

# Percent of articles with a positive sentiment
print("+sent%: " + str(t_positive / n))

# Percent of articles with a negative sentiment
print("-sent%: " + str(t_negative / n))

# Percentage of articles with sentiment
print("opinion rating: " + str((t_positive + t_negative) / n))

# Bitcoin's price
print("USD/BTC: " + str(price))