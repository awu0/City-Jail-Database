import json
from django.http import JsonResponse
from django.shortcuts import render
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic
from jail.models import User
import hashlib

def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get("username", "")
        password = data.get("password", "")

        user = User.objects.get(username=username)

        stored_hashed_password = user.password

        hashed_password = str(hashlib.sha256(password.encode()).hexdigest())

        if hashed_password == stored_hashed_password:
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
            hashed_password = str(hashlib.sha256(password.encode()).hexdigest())
            User.objects.create(username=username,password=hashed_password)

        return JsonResponse({'message': 'Registration successful'}, status=200)
    else:
        return render(request, 'login/signup.html')
