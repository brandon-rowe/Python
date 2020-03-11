#testing web scraping
import requests
import bs4
from bs4 import BeautifulSoup

def main():
        #use requests for get, put, post, delete
        response = requests.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/')
        txt = open("coinmarketdata.txt", 'w')
        with open('coinmarket.html', 'w') as f:
                data = response.text
                soup = BeautifulSoup(data, 'html.parser')
                txt.write(soup.tbody.prettify())
                f.write(data)
                f.close()
                txt.close()

main()


