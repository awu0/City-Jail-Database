import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic
from jail.models import User

def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get("username", "")
        password = data.get("password", "")

        user = User.objects.filter(username=username,password=password)

        if user.exists():
            user = user.first()
            request.session["user"] = {
                'id': user.id,
                'username': user.username,
            }
            return JsonResponse({'message': "Login successful"}, status=200)
        else:
            return JsonResponse({'message': "Username or password incorrect"}, status=400)
    else:
        return render(request, 'login/login.html')

def signout(request):
    request.session.flush()
    return render(request, 'login/login.html') 

def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get("username", "")
        password = data.get("password", "")

        if username == "" or password == "":
            return JsonResponse({'message': 'Username or password cannot be blank'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'message': 'This username already exists.'}, status=400)
        else:
            User.objects.create(username=username,password=password)

        return JsonResponse({'message': 'Registration successful'}, status=200)
    else:
        return render(request, 'login/signup.html')