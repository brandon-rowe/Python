#testing web scraping
import requests

def main():
        #use requests for get, put, post, delete
        response = requests.get('https://httpbin.org/ip')
        print('Your IP is {0}'.format(response.json()['origin']))
        r = requests.get('https://api.github.com/events')
        r.text
        r.content
        
        with open('log.txt', 'w') as f:
                data = r.text
                f.write(data)
                f.close()

        with open('log.txt','ab') as f:
                extra = r.content
                f.write(extra)
                f.close()
                
        r = requests.put('https://httpbin.org/put', data={'key':'value'})
        r = requests.delete('https://httpbin.org/delete')
        r = requests.head('https://httpbin.org/get')
        r = requests.options('https://httpbin.org/get')
        #Code below will add keys & values to end of URL
        payload = {'key1':'value1', 'key2':'value2'}
        r = requests.get('https://httpbin.org/get', params=payload)
        print(r.url)
main()


