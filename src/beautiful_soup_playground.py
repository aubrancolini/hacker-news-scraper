import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    response = requests.get("https://news.ycombinator.com/news")
    soup = BeautifulSoup(
        response.text, "html.parser"
    )  # bs4 parses the response to html
    print(soup.find_all("div"))
    print(soup.find_all("a"))  # a for links
    print(soup.find("a"))  # only find the first link
    print(soup.select(".score"))  # selects items wiht class = "score"
    print(soup.select(".titleline"))
    print(
        soup.select(".titleline")[0]
    )  # select the first item with class = "titleline"

    titles = soup.select(".titleline")
    scores = soup.select(".score")

    # selects first title link and score
    print(f"{titles[0].find('a')} {scores[0].contents}")
