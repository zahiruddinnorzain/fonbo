from bs4 import BeautifulSoup
import requests

'''

# show all post
source = requests.get('https://www.gsmarena.com/oppo-phones-82.php').text
soup = BeautifulSoup(source, 'lxml')

# linkposts = soup.find_all('div', class_='makers')
linkposts = soup.find_all('li')

# print(linkposts)

for linkpost in linkposts[16:]:

	# get link for one post
	link = linkpost.a['href']
	print(link)
'''
source2 = open('index.html')
soup2 = BeautifulSoup(source2, 'lxml')
# print(f'https://www.gsmarena.com/{link}')

specs = soup2.find_all('td', class_='nfo')
titlespecs = soup2.find_all('td', class_='ttl')

for spec in specs:
	print(spec.text)

for titlespec in titlespecs:
	print(titlespec.text)