from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def api2():
	# titles = []
	specin = []
	specin2 = []

	if (request.method == 'POST'):
		# some_json = request.get_json()
		url1 = request.form['url1']
		url2 = request.form['url2']


		# source = requests.get(url1).text
		source = open(url1)
		soup = BeautifulSoup(source, 'lxml')
		# print(f'https://www.gsmarena.com/{link}')

		specs = soup.find_all('td', class_='nfo')
		titlespecs = soup.find_all('td', class_='ttl')

		for spec in specs:
			# print(spec.text)
			specin.append(spec.text)


		# source2 = requests.get(url2).text
		source2 = open(url2)
		soup2 = BeautifulSoup(source2, 'lxml')
		# print(f'https://www.gsmarena.com/{link}')

		specs = soup2.find_all('td', class_='nfo')
		titlespecs = soup2.find_all('td', class_='ttl')

		for spec in specs:
			# print(spec.text)
			specin2.append(spec.text)


		# return jsonify({'you get': specin}), 201
		return render_template('index.html', specin=specin, specin2=specin2)
	else:
		# return jsonify({"about":"hello semua"})
		return render_template('index.html', specin=specin, specin2=specin2)

if __name__=='__main__':
	app.run(debug=True)


# @app.route('/')
# def about():
	# source = requests.get('http://www.moh.gov.my/index.php/pages/view/2019-ncov-wuhan').text
	# soup = BeautifulSoup(source, 'lxml')
	# pic = soup.find('img', alt='status-terkini-covid19')['src']
	# full_pic = 'http://www.moh.gov.my/' + str(pic)

	# source = requests.get('http://covid-19.moh.gov.my/').text
	# soup = BeautifulSoup(source, 'lxml')
	# pic = soup.find('img', class_='tm-image jl-box-shadow-hover-medium')['src']
	# full_pic = 'http://covid-19.moh.gov.my/' + str(pic)


##barui sekali
	# titles = []
	# specin = []
	# # imgs = []


	# source2 = open('index.html')
	# soup2 = BeautifulSoup(source2, 'lxml')
	# # print(f'https://www.gsmarena.com/{link}')

	# specs = soup2.find_all('td', class_='nfo')
	# titlespecs = soup2.find_all('td', class_='ttl')

	# for spec in specs:
	# 	print(spec.text)
	# 	specin.append(spec.text)

	# for titlespec in titlespecs:
	# 	print(titlespec.text)
	# 	titles.append(titlespec.text)

	# return render_template('index.html', specin=specin, titles=titles)



'''
	# show all post
	# https://resepicheain.blogspot.com/search?max-results=213
	source = requests.get('https://resepicheain.blogspot.com/search?max-results=213').text
	soup = BeautifulSoup(source, 'lxml')

	# get all url post
	# linkpost = soup.find_all('div', class_='snippet-thumbnail').a['href']
	linkposts = soup.find_all('div', class_='snippet-thumbnail')
	# print(linkpost)

	# show all link post
	for linkpost in linkposts:

		# get link for one post
		link = linkpost.a['href']
		print(link)

		# crawl by post
		source2 = requests.get(link).text
		soup2 = BeautifulSoup(source2, 'lxml')

		# print(soup2.prettify())

		# get pic
		picpost = soup2.find('div', class_='separator').a['href']
		print(picpost)
		imgs.append(picpost)

		# get title post
		titlepost = soup2.find('h3', class_='post-title entry-title').text
		print(titlepost)
		titles.append(titlepost)

		# get text post with no text but html, nak text type .text
		bodypost = soup2.find('div', class_='post-body entry-content float-container').text
		print(bodypost)
		bodys.append(bodypost)
	# context = {
 #        'titles':titles,
 #        'bodys':bodys,
 #        'imgs': imgs,
 #    }

	# return render_template('index.html', specin=specin)
'''
# if __name__=='__main__':
# 	app.run(debug=True)