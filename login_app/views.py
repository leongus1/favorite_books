from django.shortcuts import render, redirect
from login_app.models import Users
import bcrypt

from django.contrib import messages

# Create your views here.
def index(request):
    
    return render(request, 'index.html')
    
def check_log(request):
    if len(Users.objects.filter(email=request.POST['email']))==0:
        request.session['invalid_user_email']="No account with this email address"
        return redirect('/')
    else:
        hash = Users.objects.get(email=request.POST['email']).password_hash
        if bcrypt.checkpw(request.POST['pw'].encode(), hash.encode()):
            user1 = Users.objects.get(email=request.POST['email'])
            request.session['pw_match'] = 'password match'
            request.session['user_id'] = user1.id
            request.session['name']=user1.first_name
           
            return redirect ('/books')
        else:
            print('password doesnt match')
            request.session['bad_pw']="Invalid Password"
            return redirect('/')

#create or update records 
def register(request):
    # context = {}
    errors = Users.objects.user_validator(request.POST)
    
    if len(Users.objects.filter(email=request.POST['email'])) > 0:
        errors['acct_status']="There is already an account using this email address."
    
    if errors:
        for key, values in errors.items():
            messages.error(request, values)
        return redirect('/')
    else:        
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        Users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password_hash=pw_hash)
        request.session['acct_status']='Account successfully created'
        user1 = user1 = Users.objects.get(email=request.POST['email'])
        request.session['user_id'] = user1.id
        request.session['name']=user1.first_name
        
        return redirect('/books')

def logout(request):
    request.session.flush()
    return redirect('/')