from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User,Booking, Discount

class CustomUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','password']

        widgets = {
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'password': forms.PasswordInput(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = []

        widgets = {
            'first_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'password': forms.PasswordInput(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'avatar': forms.ClearableFileInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'dob': forms.DateInput(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                    'type': 'date'
                }
            ),
            'country': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'state': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'area_code': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'gender': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'phone': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
        }
    
class  BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['address']

        widgets = {
            'address': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                    'rows': 2,
                    'cols': 2,
                }
            )
        }

class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = '__all__'
        exclude = ['client']

        widgets = {
            'client_booking_number': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                    'placeholder': '2092817272'
                }
            ),
            'discount_amount': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'required': 'required',
                    'placeholder': '3500'
                }
            )
        }