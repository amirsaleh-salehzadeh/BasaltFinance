from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, update_session_auth_hash, authenticate
from userApp.models import User
from userApp.forms import UserRegistrationForm
from django.contrib import messages
from django.http.response import HttpResponse
import json
from django.contrib.auth.decorators import login_required

def create_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userApp:login')  # Redirect to the login page
    else:
        form = UserRegistrationForm()
    return render(request, 'user/create_user.html', {'form': form})

# def user_profile(request, id):
#     user = get_object_or_404(User, pk=id)  # Retrieve user by ID or handle 404 error
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST, instance=user)
#         if user_form.is_valid():
#             user_form.save()
#             update_session_auth_hash(request, user_form.instance)  # Update the user's session
#             messages.success(request, 'Your profile was successfully updated!')
#             return redirect('user_profile')
#     else:
#         user_form = UserChangeForm(instance=request.user)
#         password_form = PasswordChangeForm(request.user)
#
#     return render(request, 'user/user_profile.html', {'user_form': user_form, 'password_form': password_form})
def login_form(request):
    response_data = {}
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            login(request, user)
        except:
            response_data['errorResult'] = "Invalid username or password"
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
    return render(request, 'login.html')

@login_required
def user_list(request):
    users = User.objects.all()  # Get all accounts
    return render(request, 'user/user_list.html', {'users': users})
