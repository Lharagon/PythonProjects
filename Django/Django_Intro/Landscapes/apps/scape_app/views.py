from django.shortcuts import render, redirect
from random import randint

# Create your views here.

def index(request):
	return render(request, 'scape_app/index.html')

def landscapes(request, num):
	try:
		num = int(num)
	except:
		print "NOT INTERGER "
		return redirect('/')
	# print isinstance(num), "WHAT num comes out as"
	if num > 50 or num <= 0:
		print "Out of range Error"
		return redirect('/')

	# if type(num) == int:
	# 	print "This kind of worked I guess"

	stock = [
	"https://cdn.shutterstock.com/shutterstock/videos/3436859/thumb/1.jpg?i10c=img.resize(height:160)",
	"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYJ8heniVYqakSuIYAnMegizWaUUV57F9hvykWhNqWEZHtwhlH",
	"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgYuKJhAat553IhBGfMPO04D496CrypIhKxI7yNCot_AXHuvc6",
	"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2GMMZ84ZrtP6ubKXeoUl4kp5cIjirlAOUoYptHEM9ntrPxngV",
	"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJbEPTKUWyIvaXSa7DNDYvDXbpqJUMMViRMDeh8-Cv2l8iS5pD",
	"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnGevXODlLngIXPVjbotPqr8zxwN5_cc4sL6X3LJiccTmeg13bsg",
	"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfP5RpoXEhP_D5disGZnE1frtTquprBfxPB9BIo-S5Ij9qftnn"
	]

	# if num < 2:
	# 	picture = stock[0]
	# elif num == 2 or num == 3:
	# 	picture = stock[randint(0, 6)]
	# 	context['photo'] = picture
	# 	return render(request, 'scape_app/landscape.html', context)
	# elif num > 3:
	# 	for numbs in range(2, num-1):
	# 		if num % numbs == 0:
	# 			continue
	# else:
	# 	picture = stock[randint(0, 6)]
	# 	context['photo'] = picture
	# 	return render(request, 'scape_app/landscape.html', context)
    

	if num > 40:
		picture = stock[4]
	elif num > 30:
		picture = stock[3]
	elif num > 20:
		picture = stock[2]
	elif num > 10:
		picture = stock[1]
	elif num > 0:
		picture = stock[0]

	context = {
		'photo': picture
	}
	print "Got to the end"
	return render(request, 'scape_app/landscape.html', context)