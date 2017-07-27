from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'ninjas_app/index.html')

def ninjas(request):
	context = {
		'ninja' : 'ninjas_app/imgs/tmnt.png'
	}

	return render(request,'ninjas_app/ninjas.html', context)

def ninjs(request, ninj):
	

	if ninj == "blue":
		choice = 'ninjas_app/imgs/leonardo.jpg'
	elif ninj == "orange":
		choice = 'ninjas_app/imgs/michelangelo.jpg'
	elif ninj == "red":
		choice = 'ninjas_app/imgs/raphael.jpg'
	elif ninj == "purple":
		choice = 'ninjas_app/imgs/donatello.jpg'
	else:
		choice = 'ninjas_app/imgs/notapril.jpg'
	
	context = {
		'ninja' : choice
	}

	return render(request,'ninjas_app/ninjas.html', context)
	

# def ninjs(request):
# 	pass