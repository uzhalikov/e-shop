from .forms import UserRegistrationForm, UserAuthForm

def user_reg_form(request):
    return {'user_reg_form': UserRegistrationForm()}

def user_auth_form(request):
    return {'user_auth_form': UserAuthForm()}