from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.



def index(request):
    
    
    return render(request, 'index.html')

def home(request):
    return render(request, 'base.html')
    pass

def register(request, *args, **kwargs):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        mail = request.POST['mail']
       
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
               messages.info(request, 'username taken')
               return redirect('register')
            elif User.objects.filter(email=mail).exists():
                messages.info(request,'email taken')
            else:        
                user = User.objects.create_user(username=username, password=password1, email=mail, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request,"wrong password")
            return redirect('register')    
        return redirect('/')
        
    else:
        return render(request, 'register.html')

    pass
def login(request, *args, **kwargs):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'invalid details')
            return redirect('login')
        
    else:
            
        return render(request, 'login.html')
    pass
def about(request, *args, **kwargs):
    return render(request, 'about.html')

    pass
def contact(request, *args, **kwargs):
    return render(request, 'contact.html')

    pass
def course(request, *args, **kwargs):
    return render(request, 'course.html')

    pass
def detail(request, *args, **kwargs):
    return render(request, 'detail.html')

    pass
def feature(request, *args, **kwargs):
    return render(request, 'feature.html')

    pass
def team(request, *args, **kwargs):
    return render(request, 'team.html')

    pass
def testimonial(request, *args, **kwargs):
    return render(request, 'testimonial.html')

    pass

def message(request):
    pass

def logout(request):
    auth.logout(request)
    return redirect('/')