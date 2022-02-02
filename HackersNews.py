import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://news.ycombinator.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all(attrs={ 'class': 'titlelink' })
    for title in titles:
        try:
            print(f"    title: {title.contents[0]}    link: {title.attrs['href']}")
        except KeyError:
            pass


if __name__ == '__main__':
    main()
