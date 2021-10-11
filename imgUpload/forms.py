from django import  forms

class ImageUpoadForm(forms.Form):
    image = forms.ImageField()