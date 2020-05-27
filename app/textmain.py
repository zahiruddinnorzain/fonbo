from bs4 import BeautifulSoup
import requests

# show all post
# https://resepicheain.blogspot.com/search?max-results=213

# source = requests.get('https://resepicheain.blogspot.com/search?max-results=213').text

# soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

# title = soup.find('title')

#pic = soup.find('img', alt='status-terkini-covid19')['src']

# print(pic)

#full_pic = 'http://www.moh.gov.my/' + str(pic)

#print(full_pic)

# get picpost
# salah
# pic = soup.find('img', alt='Image')['src']
# print(pic)

# print('-----')

# titles = []
# bodys = []
# imgs = []
# thisdict = {}

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

	source2 = requests.get(f'https://www.gsmarena.com/{link}').text
	soup2 = BeautifulSoup(source2, 'lxml')
	# print(f'https://www.gsmarena.com/{link}')

	specs = soup2.find_all('td', class_='nfo')
	titlespecs = soup2.find_all('td', class_='ttl')

	for spec in specs:
		print(spec.text)

'''

# get all url post
# linkpost = soup.find_all('div', class_='snippet-thumbnail').a['href']
linkposts = soup.find_all('div', class_='snippet-thumbnail')
# print(linkpost)

# show all link post
for linkpost in linkposts:

	# get link for one post
	link = linkpost.a['href']
	# print(link)

	# crawl by post
	source2 = requests.get(link).text
	soup2 = BeautifulSoup(source2, 'lxml')

	# print(soup2.prettify())

	# get pic
	picpost = soup2.find('div', class_='separator').a['href']
	print(picpost)
	# imgs.append(picpost)

	# get title post
	titlepost = soup2.find('h3', class_='post-title entry-title').text
	print(titlepost)
	# titles.append(titlepost)

	# get text post with no text but html, nak text type .text
	bodypost = soup2.find('div', class_='post-body entry-content float-container').text
	print(bodypost)
	# bodys.append(bodypost)

	# thisdict["picpost"] = picpost
	# thisdict["titlepost"] = titlepost
	# thisdict["bodypost"] = bodypost

print(thisdict)

# print(title)

'''