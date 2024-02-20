from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from fms.settings import MEDIA_ROOT, MEDIA_URL
from django.contrib import messages

#login
def login_user(request):
    logout(request)
    username = ''
    password = ''
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("home")
            else:
                messages.warning(request, "User is inactive. Please contact respective admin!")
                return redirect("login")
        else:
            messages.warning(request, "Incorrect username or password!")
            return redirect("login")
    else:
        return render(request, "login.html", {})
    
#logout_user
@login_required
def logout_user(request):
    logout(request)
    messages.info(request, "you have successfully logged out!")
    return redirect("login")
