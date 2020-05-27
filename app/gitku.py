import os

def cuci():
	os.system('clear')

cuci()
while True:
	print('===============')
	print('=====GITKU=====')
	print(' 0 = git pull')
	print(' 1 = git add .')
	print(' 2 = git commit -m')
	print(' 3 = git push')
	print(' 4 = git add & commit')
	print(' 5 = git init')
	print(' 6 = git status')
	print('19 = exit')

	jwp = input('Ans: ')

	if jwp == "1":
		cuci()
		os.system('git add .')
		print('Done add')

	elif jwp == "2":
		note = input("comment : ")
		cuci()
		os.system("git commit -m '" + note + "'")

	elif jwp == "3":
		cuci()
		os.system('git push')

	elif jwp == "4":
		cuci()
		os.system('git add .')
		print('Done add')
		note = input("comment : ")
		os.system("git commit -m '" + note + "'")

	elif jwp == "5":
		cuci()
		os.system('git init')

	elif jwp == "6":
		cuci()
		os.system('git status')

	elif jwp == "0":
		cuci()
		os.system('git pull')

	elif jwp == "19":
		cuci()
		break

	else:
		os.system('git ' + jwp)
