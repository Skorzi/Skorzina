from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class BasketAddProductForm(forms.Form):
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )


class createUserForm(UserCreationForm):

    email = forms.EmailField(max_length=200, help_text='Required', error_messages={
                             'invalid': 'Error Missing Field , Please Fill this Field'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).count() > 0 and email:
            raise forms.ValidationError("Error Missing Field , Please Fill this Field")
        else:
            return email


class authForm(AuthenticationForm):
    class Meta():
        model = User
        fields = ['username', 'password']
