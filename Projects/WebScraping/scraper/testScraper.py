import requests

def main():
	response = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
	print('Your IP is {0}'.format(response.json()['origin']))

main()
