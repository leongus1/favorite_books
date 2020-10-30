from django.shortcuts import render, redirect, HttpResponse
from  login_app.models import Users
from books_app.models import Books
from django.contrib import messages

# Create your views here.


#RENDER
def index(request):
    request.session['updated_message'] = ""
    context={
        'books': Books.objects.all(),
        'user': Users.objects.get(id=request.session['user_id'])
    }
    return render(request, 'book_index.html', context)

def book_details(request, book_id):
    context = {
        'book': Books.objects.get(id=book_id),
        'user': Users.objects.get(id=request.session['user_id'])
    }
    return render(request, "book_details.html", context)

#DATA PROCESSING
def create_book(request):
    errors = Books.objects.book_validator(request.POST)
    if errors:
        for key, values in errors.items():
            messages.error(request, values)
        return redirect('/books')
    if request.method == "POST":
        book1 = Books.objects.create(title=request.POST['title'], description=request.POST['description'], uploaded_by=Users.objects.get(id=request.session['user_id']))
        book1.users_who_like.add(Users.objects.get(id=request.session['user_id']))
        book1.save()
        return redirect('/books')
    else:
        return redirect('/books')
    
def like_book(request, book_id):
    request.session['updated_message'] = ""
    Books.objects.get(id=book_id).users_who_like.add(Users.objects.get(id=request.session['user_id']))
    return redirect(f'/books/{book_id}')

def unlike_book(request, book_id):
    request.session['updated_message'] = ""
    Books.objects.get(id=book_id).users_who_like.remove(Users.objects.get(id=request.session['user_id']))
    return redirect(f'/books/{book_id}')

def update_book(request, book_id):
    if request.method == "POST":
        book1 = Books.objects.get(id=book_id)
        book1.title = request.POST['title']
        book1.description = request.POST['description']
        book1.save()
        request.session['updated_message'] = "Book updated"
    return redirect (f"/books/{book_id}")

def delete_book(request, book_id):
    request.session['updated_message'] = ""
    print('request to delete, right before')
    book1 = Books.objects.get(id=book_id)
    book1.delete()
    print('processed the delete command')
    return redirect('/books')

def user_favorites(request):
    context = {
        'user': Users.objects.get(id=request.session['user_id'])
    }
    return render(request, 'userfavs.html', context)
    
    
    
