from django.shortcuts import redirect
from django.urls import resolve

class SessionCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        resolved_path = resolve(request.path_info)
        excluded_views = ['login', 'signup']
        if resolved_path.url_name not in excluded_views:
            if 'user' not in request.session:
                return redirect('login')
            
        response = self.get_response(request)
        return response