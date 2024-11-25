from django.contrib.auth import get_user_model
from django import forms
User = get_user_model()

class UserAuthForm(forms.ModelForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'autocomplete': 'off'}))

    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Логин')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    email = forms.EmailField(label='Электронная почта')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'autocomplete': 'off'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'autocomplete': 'off'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        elif cd['password'] in cd['username']:
            raise forms.ValidationError('Ваш пароль содержит ваш логин')
        return cd['password']