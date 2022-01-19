
import csv
import requests
from bs4 import BeautifulSoup

response = requests.get('http://quotes.toscrape.com/')# mb .text here would be more readable?!
html_data = BeautifulSoup(response.text, 'html.parser')
quotes = html_data.find_all(class_="quote")

with open('scrap2scv.scv', 'w') as file:
	csv_writer = csv.DictWriter(file, fieldnames= ['Quote','Text','Tags'])
	csv_writer.writeheader()
	for quote in quotes:
		csv_writer.writerow({
			'Quote': quote.find(class_='text').text, 
			'Text' : quote.find(class_='author').text,
			'Tags' : quote.find(class_='keywords')["content"]})