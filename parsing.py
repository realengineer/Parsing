from bs4 import BeautifulSoup
import urllib

data = urllib.urlopen('http://www.maincoupon.com/')
soup = BeautifulSoup(data, 'html.parser')
offers = soup.find_all("span", "url")

for i in range (0,len(offers)): 
	print offers[i].string         
