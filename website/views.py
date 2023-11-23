
from django.shortcuts import redirect, render
from django.contrib.auth  import authenticate, login, logout
from django.contrib import messages


def home(request):
  # check to seee if logging in
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    
    # Authemticate
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, "Welcome, You are Logged In!")
      return redirect('home')
    else: 
      messages.success(request, "There was an error Logged In, Please try again...")
      return redirect('home')
  else: 
      return render(request, 'home.html',{})



# def login_user(request): 
#   pass
 
    
def logout_user(request): 
  pass