from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('cabinet')
      
        else:

            # Return an 'invalid login' error message.
            messages.success(request,("There was an error logging in. Please try again"))
            return redirect('logi')
    else:
        return render(request, 'login.html', {})
    
@login_required
def cabinet(request):
    all_keys = Key.objects.all()
    current_user = User.objects.get(username=request.user)
    return render(request, 'cabinet.html', {'keys': all_keys, 'user': current_user})

def take_key(request, key_id):
    key = Key.objects.get(id=key_id)
    current_user = User.objects.get(username=request.user)
    print(current_user)
    current_user_role = UserRole.objects.filter(user=current_user).first()
    print(current_user_role)
    current_role = Role.objects.filter(type=current_user_role.role.type).first()
    print(current_role)
    permission = Permission.objects.filter(role=current_role, key=key).first()
    print(permission)
    if key.quantity > 0:
        if permission and permission.level == 'Write':
            key.quantity -= 1
            key.save()
            new_access = Access(user=current_user, key=key)
            new_access.save()
            messages.success(request, f"Key {key.keyname} obtained by {current_user.username}")
        else:
            messages.success(request, f"You do not have permission to access {key.keyname}")
    else:
        messages.success(request, f"No more {key.keyname} keys available")
    
    return redirect('cabinet')

def return_key(request, key_id):
    current_user = User.objects.get(username=request.user)
    key = Key.objects.get(id=key_id)
    access = Access.objects.filter(user=current_user, key=key, returnDateTime=None).first()

    if access:
        access.returnDateTime = datetime.now()
        access.save()
        key.quantity += 1
        key.save()
        messages.success(request, f"Key {key.keyname} returned by {current_user.username}")
    else:
        messages.success(request, f"You do not have {key.keyname} key")

    return redirect('cabinet')

def logout_user(request):
    logout(request)
    messages.success(request,("You have been logged out"))
    return redirect('logi')