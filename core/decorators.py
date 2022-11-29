from django.http import HttpResponse
from django.shortcuts import redirect

def unauthorised_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def admin_view(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_admin:
            return redirect('dashboard')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
