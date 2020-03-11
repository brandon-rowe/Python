#testing web scraping
import requests
import bs4
from bs4 import BeautifulSoup

def main():
        #use requests for get, put, post, delete
        response = requests.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end=20200311')
        txt = open("coinmarketdata.txt", 'w')
        with open('coinmarket.html', 'w') as f:
                data = response.text
                soup = BeautifulSoup(data, 'html.parser')
                td = soup.find_all('td')
                for i in td:
                    value = i.contents[0].contents[0]
                    input = value + "|"
                    txt.write(str(input))
                f.write(data)
                f.close()
                txt.close()

main()


