import functools
from django.shortcuts import redirect

def doctor_required(view_func):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.role == 1:
            return view_func(request, *args, **kwargs)
        return redirect('home')
        
    return wrapper


def client_required(view_func):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.role == 2:
            return view_func(request, *args, **kwargs)
        return redirect('home')
        
    return wrapper


def confirmed_client_required(view_func):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.role == 2 and request.user.confirmed:
            return view_func(request, *args, **kwargs)
        return redirect('home')
        
    return wrapper