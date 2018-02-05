# Bitcoin Sentiment Analysis
## Goal
Investigate a connection between mass-media sentiment of Bitcoin and its value over time (regardless of whether that connection is based on causation or correlation).
## What it does
* Uses [NewsAPI](https://newsapi.org/) to fetch all articles from the past 24 hours that mention Bitcoin
* Adds up the number of positive and negative words per article title from modified [word lists compiled by Minqing Hu and Bing Liu from the University of Illinois at Chicago](https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html) (see citations 1 and 2) to get a net for that article (a positive number or negative number)
* Finds the percentage/ratio of sentiment that day
* Gets Bitcoin's closing price from the previous day
* Find the percentage agreement between price and sentiment to determine if a connection exists
* Exports this data to a CSV

## Requirements
* Python 3.x
* [NewsApi api key](https://newsapi.org/)
* [NewsAPI python wrapper](https://github.com/SlapBot/newsapi)

## Citations
1. Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, Washington, USA.
2. Bing Liu, Minqing Hu and Junsheng Cheng. "Opinion Observer: Analyzing and Comparing Opinions on the Web." Proceedings of the 14th International World Wide Web conference (WWW-2005), May 10-14, 2005, Chiba, Japan.