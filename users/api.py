from .forms import UserRegistrationForm, UserAuthForm
from django.http.response import JsonResponse
from .utils import generate_password
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as log_in, logout as log_out


def logout(request):
    log_out(request)
    return redirect('/')


def login(request):
    form = request.POST
    status = 401
    user = authenticate(username=form['username'], password=form['password'])
    if user:
        log_in(request, user)
        status = 200
    return JsonResponse(status, safe=False)

def register(request, fast_create=False):
    data = request.POST
    if fast_create:
        password = generate_password()
        data = data.copy()
        data.update({'password': password, 'password2': password, 'username': data['email']})

    form = UserRegistrationForm(data)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        if fast_create:
            return user
        return login(request)
    return JsonResponse(401, safe=False)