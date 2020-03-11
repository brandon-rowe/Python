#testing web scraping
import requests
import bs4

def main():
        #use requests for get, put, post, delete
        response = requests.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/')
        response.text
        response.content
        
        with open('log.txt', 'w') as f:
                data = response.text
                f.write(data)
                f.close()

        with open('log2.txt','ab') as f:
                extra = response.content
                f.write(extra)
                f.close()
                
        payload = {'key1':'value1', 'key2':'value2'}
        r = requests.get('https://httpbin.org/get', params=payload)
        print(r.url)
main()


