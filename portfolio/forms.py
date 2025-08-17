from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label="نام",
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'نام شما'})
    )
    email = forms.EmailField(
        label="ایمیل",
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'ایمیل شما'})
    )
    message = forms.CharField(
        label="پیام",
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'متن پیام'})
    )
