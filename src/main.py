"""
Scraps first two pages of Hacker news.
Selects only title, link and score of articles with 100 or more votes.
Prints the result to the console.
"""

import requests
from bs4 import BeautifulSoup


def sort_articles_by_score(articles):
    # Sort articles by score

    # lambda is to tell sorted function the dictionary key it must use to sort
    return sorted(articles, key=lambda k: k["score"], reverse=True)


def popular_articles(titles, subtexts):
    # selects only articles with 100 or more votes

    articles = []

    # Zips together the two list so we can loop.
    for title, subtext in zip(titles, subtexts):
        if subtext.select(".score"):  # sometimes there is no class score
            score = int(subtext.select(".score")[0].getText().replace(" points", ""))
            if score >= 100:  # only popular articles
                text = title.find("a").get_text(strip=True)
                link = title.find("a")["href"]
                articles.append({"text": text, "link": link, "score": score})

    return sort_articles_by_score(articles)


all_titles = []
all_subtexts = []

# Loop to scrap more than one page
for page in range(1, 3):
    response = requests.get(f"https://news.ycombinator.com/news?p={page}")
    soup = BeautifulSoup(response.text, "html.parser")

    titles = soup.select(".titleline")
    subtexts = soup.select(".subtext")
    all_titles.extend(titles)
    all_subtexts.extend(subtexts)

popular_article = popular_articles(all_titles, all_subtexts)

# Prints to console only popular article
for i in popular_article:
    print(f"Title: {i['text']} | Link: {i['link']} | Score: {i['score']}")
