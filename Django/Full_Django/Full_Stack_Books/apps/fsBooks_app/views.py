from django.shortcuts import render, redirect
from .models import Book

# Create your views here.
def index(request):
	books = Book.objects.all()

	context = {
		'book_list' : books
	}
	return render(request, "fsBooks_app/index.html", context)

def add(request):
	title = request.POST['title']
	category = request.POST['category']
	author = request.POST['author']

	Book.objects.create(title = title, category = category, author = author)

	return redirect('/')