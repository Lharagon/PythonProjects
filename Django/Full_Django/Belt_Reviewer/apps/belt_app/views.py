from django.shortcuts import render, redirect
from .models import User, Author, Review, Book
from django.contrib import messages
import bcrypt

# Create your views here.

def index(request):
	# if 'user' in request.session:
	# 	return redirect('/books')
	return render(request, 'belt_app/index.html')

def books(request):

	context = {
		"books" : Book.objects.order_by("title"),
		"reviews" : Review.objects.order_by("-created_at")[:6]
	}

	return render(request, 'belt_app/books.html', context)

def login(request):
	if request.method == 'POST':
		validated = User.objects.Log_validator(request.POST, request)
	
		if validated:
			user = User.objects.get(email=request.POST['email'])
			request.session['user'] = user.alias
			request.session['user_id'] = user.id
			return redirect('/books')
	
		return redirect('/')

	return redirect('/')

def register(request):
	if request.method == 'POST':
		validated = User.objects.Reg_validator(request.POST, request)
		if validated:
			hashed_pass = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
			print "This is the hashed_ass at register", hashed_pass
			user = User.objects.create(full_name = request.POST['full_name'], alias = request.POST['alias'], email = request.POST['email'], password =hashed_pass)
			request.session['user'] = user.alias
			request.session['user_id'] = user.id
			return redirect('/books')

		return redirect('/')

	return redirect('/')

def log_out(request):
	# if request.method == 'POST':
	request.session.clear();
	messages.success(request, "Hurry Back!!!!")
	return redirect('/')

def add(request):
	author_list = Author.objects.all()
	context = {
		'author_list': author_list
	}
	return render(request, 'belt_app/add.html', context)


def add_book(request):
	if len(request.POST['new_author']) > 0 or len(request.POST['ex_author']) > 0:

		book = Book.objects.filter(title = request.POST['title'])
	
		if book:
			messages.error(request, "This book already exist")
			return redirect('/add')
		author = Author.objects.filter(name = request.POST['new_author'])
		if author:
			messages.error(request, "This author already exists")
			return redirect('/add')
	
		if len(request.POST['new_author']) > 0:
			book_author = Author.objects.create(name = request.POST['new_author'])
		else:
			book_author = Author.objects.get(id = request.POST['ex_author'])


		user = User.objects.get(id = request.session['user_id'])
		new_book = Book.objects.create(title = request.POST['title'], author = book_author)
		new_review = Review.objects.create(content = request.POST['review'], reviewer = user, book_reviewed = new_book, rating = int(request.POST['rating']))
	
		return redirect('/books')

	else:
		messages.error(request, "You need to include an author")
		return redirect('/books')

def book_pro(request, id):
	book = Book.objects.get(id = id)
	reviews = Review.objects.filter(book_reviewed = book).order_by('-created_at')

	context = {
		"book" : book,
		"reviews" : reviews
	}

	return render(request, 'belt_app/bookpro.html', context)

def add_review(request, id):
	book = Book.objects.get(id = id)
	user = User.objects.get(id = request.session['user_id'])
	new_review = Review.objects.create(content = request.POST['review'], reviewer = user, book_reviewed = book, rating = int(request.POST['rating']))

	return redirect('/book_pro/%s' % (id))

def user_pro(request, id):
	pro_user = User.objects.get(id = id)
	user_reviews = Review.objects.filter(reviewer = pro_user)

	context = {
		"pro_user": pro_user,
		"user_reviews":  user_reviews,
		"rating_system": [1,2,3,4,5] 
	}

	return render(request, 'belt_app/users.html', context)

def delete(request, id, bid):
	Review.objects.get(id = id).delete()
	return redirect('/book_pro/%s' % bid)





