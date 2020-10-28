from django.shortcuts import render, redirect, HttpResponse
from  login_app.models import Users
from books_app.models import Books

# Create your views here.


#RENDER
def index(request):
    context={
        'books': Books.objects.all()
    }
    return render(request, 'book_index.html', context)

def book_details(request, book_id):
    context = {
        'book': Books.objects.get(id=book_id)
    }
    return render(request, "book_details.html", context)

#DATA PROCESSING
def create_book(request):
    Books.objects.create(title=request.POST['title'], description=request.POST['description'], uploaded_by=Users.objects.get(id=request.session['user_id']))
    
    # book1.users_who_like.add(request.session['user_id'])
    # book1.save()
    return redirect('/books')
    
    
def like_book(request, book_id):
    Books.objects.get(id=book_id).users_who_like.add(Users.objects.get(id=request.session['user_id']))
    return redirect(f'/books/{book_id}')

def unlike_book(request, book_id):
    Books.objects.get(id=book_id).users_who_like.add(Users.objects.remove(id=request.session['user_id']))
    return redirect(f'/{book_id}')

def update_book(request, book_id):
    book1 = Books.objects.get(id=book_id)
    book1.title = request.POST['title']
    book1.description = request.POST['description']
    book1.save()
    return redirect (f"/{book_id}")
    
    
    
