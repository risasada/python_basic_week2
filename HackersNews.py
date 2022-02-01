import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://news.ycombinator.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all(class_='title')
    for link in links:
            try:
                print(f"title: {link.contents[0]}")
                print(f"link: {link.attrs['href']}")
            except KeyError:
                pass


if __name__ == '__main__':
    main()
