from flask import Flask, render_template, request, jsonify, send_file
from bs4 import BeautifulSoup
import requests
import csv

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def api2():
	# titles = []
	specin = []
	specin2 = [] 
	model='&nbsp;'
	model2='&nbsp;'

	if (request.method == 'POST'):
		# some_json = request.get_json()
		url1 = request.form['url1']
		url2 = request.form['url2']




		# PHONE 1
		source = requests.get(url1).text
		# source = open(url1)
		soup = BeautifulSoup(source, 'lxml')

		# for e in soup.findAll('br'):
		# 	# e.extract()
		# 	e.replace_with(' ')
		# for e in soup.findAll('\n'):
		# 	# e.extract()
		# 	e.replace_with(' ')

		# print(f'https://www.gsmarena.com/{link}')

		specs = soup.find_all('td', class_='nfo')
		model = soup.find('h1', class_='specs-phone-name-title').text
		# titlespecs = soup.find_all('td', class_='ttl')

		# save name to link
		specin.append(model)

		for spec in specs:
			# print(spec.text)
			# entry = spec.text.strip()
			# print(entry)
			specin.append(spec.text)


#-----------------------------------------------------



		# PHONE 2
		source2 = requests.get(url2).text
		# source2 = open(url2)
		soup2 = BeautifulSoup(source2, 'lxml')
		# print(f'https://www.gsmarena.com/{link}')

		specs = soup2.find_all('td', class_='nfo')
		model2 = soup2.find('h1', class_='specs-phone-name-title').text
		# titlespecs = soup2.find_all('td', class_='ttl')
		# print(specs)

		# save name to link
		specin2.append(model2)

		for spec in specs:
			# print(spec.text)
			specin2.append(spec.text)

		# SAVE CSV
		# with open('output_data.txt') as csv_file:
		# 	csv_reader = csv.reader(csv_file, delimiter=',')
		# 	line_count = 0
		# 	for row in csv_reader:
		# 		print(specin[row])

		file = open('fonbo_data.csv', 'w')
		for row in range(len(specin)):
			file.write(f'{specin[row]};{specin2[row]}\n')
		file.close()
		candownload = True


		# return jsonify({'you get': specin}), 201
		return render_template('index.html', specin=specin, specin2=specin2, candownload=candownload, model=model, model2=model2)
	else:
		# return jsonify({"about":"hello semua"})
		candownload = False
		return render_template('index.html', specin=specin, specin2=specin2, candownload=candownload, model=model, model2=model2)


@app.route('/download')
def download():
	result = send_file('fonbo_data.csv', as_attachment=True)
	return result



if __name__=='__main__':
	app.run(debug=False)


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