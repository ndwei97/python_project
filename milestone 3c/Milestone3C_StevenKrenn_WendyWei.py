
import requests
from bs4 import BeautifulSoup

def get_links():
	# Scrape the patent website
	r = requests.get('http://appft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.html&r=0&p=1&f=S&l=50&Query=aanm%2F%22carnegie+mellon%22+AND+PD%2F4%2F1%2F2016-%3E6%2F30%2F2016&d=PG01')
	content = r.text
	soup = BeautifulSoup(content,'html.parser')
	LinkList = soup.find_all('a', href=True)
	print(LinkList)


def main():
	get_links()
	
main()


