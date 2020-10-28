from django.shortcuts import render, redirect
from login_app.models import Users
import bcrypt   

# Create your views here.
def index(request):
    context={
        
    }
    return render(request, 'index.html', context)
    
def check_log(request):
    if len(Users.objects.filter(email=request.POST['email']))==0:
        return redirect('/')
    else:
        hash = Users.objects.get(email=request.POST['email']).password_hash
        if bcrypt.checkpw(request.POST['pw'].encode(), hash.encode()):
            request.session['pw_match'] = 'password match'
            request.session['user_id'] = Users.objects.get(email=request.POST['email']).id
            request.session['name']=Users.objects.get(email=request.POST['email']).first_name
            return redirect ('/books')
        else:
            print('password doesnt match')
            request.session['pw_match'] = 'password do NOT match'
            return redirect('/')

#create or update records 
def register(request):
    # context = {}
    if len(Users.objects.filter(email=request.POST['email'])) > 0:
        request.session['acct_status']="There is already an account using this email address."
        return redirect('/')
    else:        
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        Users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password_hash=pw_hash)
        request.session['acct_status']='Account successfully created'
        request.session['user_id'] = Users.objects.get(email=request.POST['email']).id
        request.session['name']=Users.objects.get(email=request.POST['email']).first_name
        return redirect('/books')

def logout(request):
    request.session.flush()
    return redirect('/')