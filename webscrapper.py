#webscrapper to get info from LinkedIn

#import block
import urllib2 as URL
from bs4 import BeautifulSoup
from selenium import webdriver

def findComments(link):
	#By-pass LinkedIn's scraper blocking
	urlopener = URL.build_opener()
	urlopener.addheaders = [('User-agent', 'Mozilla/5.0')]

	html = urlopener.open(link).read()

	#render JS/iFrame
	driver = webdriver.Firefox()
	profile_link = link
	driver.get(profile_link)
	html = driver.page_source
	
	#web crawler
	soup = BeautifulSoup(html, "lxml")
	comments = soup.findAll('Recent Updates')
	for txt in soup.find_all("li", "feed-item"):
		print(txt.get_text())

def main():
	findComments("https://www.linkedin.com/company/state_farm")
	findComments("https://www.linkedin.com/company/amazon")


main()