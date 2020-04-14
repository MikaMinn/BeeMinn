from django.forms import ModelForm, TextInput, Textarea, DateInput, Select, NumberInput, SelectDateWidget, PasswordInput, EmailInput
from .models import History, Hives, Zones
from django.forms.utils import ErrorList
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control','placeholder': 'Email'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}))

class SignUpForm(UserCreationForm):
   username = forms.CharField(
       label="Username",
       widget=forms.TextInput(
           attrs={
               "class": "form-control"
           }
       ))
   email = forms.EmailField(
       label="Email ",
       widget=forms.EmailInput(
           attrs={
               "class": "form-control"
           }
       ))
   password1 = forms.CharField(
       label="password",
       widget=forms.PasswordInput(
           attrs={
               "class": "form-control"
           }
       ))
   password2 = forms.CharField(
       label="re-enter your password",
       widget=forms.PasswordInput(
           attrs={
               "class": "form-control"
           }
       ))

   class Meta:
       model = User
       fields = ('username', 'email', 'password1', 'password2')


class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<p class="small error">%s</p>' % e for e in self])


class AddHistory(ModelForm):

    class Meta:
        model = History
        fields = ["details", "created_at"]
        widgets = {
            'created_at' : DateInput(format='%d/%m/%Y %H:%M', attrs={'class': "form-control {% if form.name.errors %}is-invalid{% endif %}", 'data-inputmask-alias':'datetime', 'data-inputmask-inputformat':'dd/mm/yyyy', 'placeholder': "Ex.: dd/mm/aaaa", "OnKeyPress":"mask('##/##/####', this)"}),
            'details' : Textarea(attrs={'class':'form-control', 'rows':4, 'placeholder':"Détaillez.."})
        }

class AddHive(ModelForm):

    class Meta:
        model = Hives
        fields = ["name", "year", "origin", "zone", "hive_type", "frame_number", "description"]
        widgets = {
            'name' : TextInput(attrs={'class': "form-control"}),
            'year' : NumberInput(attrs={'class': "form-control"}),
            'origin' : TextInput(attrs={'class': "form-control"}),
            'zone' : Select(attrs={'class': "form-control"}),
            'hive_type' : Select(attrs={'class': "form-control"}),
            'frame_number' : NumberInput(attrs={'class': "form-control"}),
            'description': Textarea(attrs={'class':'form-control', 'rows':4, 'placeholder':"Détaillez.."})
        }

class AddZone(ModelForm):

    class Meta:
        model = Zones
        exclude = ('user',)
        fields = ["name", "city", "zip_code"]
        widgets = {
            'name' : TextInput(attrs={'class': "form-control"}),
            'city' : TextInput(attrs={'class': "form-control"}),
            'zip_code' : NumberInput(attrs={'class': "form-control"}),
        }