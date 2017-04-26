
import requests
from bs4 import BeautifulSoup

def altElement(a):
    return a[::2]

def get_links():
	# Scrape the patent website
	r = requests.get('http://appft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.html&r=0&p=1&f=S&l=50&Query=aanm%2F%22carnegie+mellon%22+AND+PD%2F4%2F1%2F2016-%3E6%2F30%2F2016&d=PG01')
	content = r.text
	soup = BeautifulSoup(content,'html.parser')
	links = []
	# prints out the all the links on the site
	# as a list
	for link in soup.find_all('a'):
	    links.append(link.get('href'))

	print(*links, sep='\n\n')

	header = 'http://appft.uspto.gov/'

	#print(len(links))
	#print(header + links[9])
	for link in links:
		if 8 < links.index(link) < 39:
			if (links.index(link)%2 == 1):
				newlink = requests.get(header + link)

				content =  newlink.text

				newlinksoup = BeautifulSoup(content,'html.parser')

				fileout = open('output.txt', 'a')
				fileout.write(newlinksoup.get_text())




def main():
	get_links()

main()
