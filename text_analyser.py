import newspaper

cnn_paper = newspaper.build('https://news.google.com/')
count = 0
array = []
for article in cnn_paper.articles:
    if len(array)<5:
        if "news.google" not in article.url: 
            array.append(article.url)
    else:
        break

print(array)
