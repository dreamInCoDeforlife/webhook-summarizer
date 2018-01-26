from bs4 import BeautifulSoup
from text_summarizer import FrequencySummarizer
import requests
import newspaper
from newspaper import Article


def news_articles():
        cnn_paper = newspaper.build('https://news.google.com/')
        count = 0
        array_url = []
        for article in cnn_paper.articles:
            if len(array_url)<5:
                if "news.google" not in article.url:
                        array_url.append(article.url)
            else:
                break
        return(array_url)
def getTextFromURL(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "html.parser")
	text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
	return text

def summarizeURL(url, total_pars):
	url_text = getTextFromURL(url).replace(u"Â", u"").replace(u"â", u"")

	fs = FrequencySummarizer()
	final_summary = fs.summarize(url_text.replace("\n"," "), total_pars)
	return " ".join(final_summary)

def article_summarize(url_link):
        article = Article(url_link)
        article.download()
        article.parse()
        article.nlp()
        summary = article.summary

        

        return(article.title+"\n"+summary)
def url(some_random):
        url = some_random
        array = news_articles()
        summary = []
        a = article_summarize(some_random)
        return (a)
        '''
        info = (a[:636] + '..')
        if len(a) > 640:
                return (info)
        else:
                return(a)
        
        b = article_summarize(array[1])
        c = article_summarize(array[2])
        d = article_summarize(array[3])
        e = article_summarize(array[4])
        '''
