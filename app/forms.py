from django import forms
from . import models


class TagForm(forms.ModelForm):
    class Meta:
        model = models.Tags
        fields = ['tag']
        widgets = {
            'tag': forms.TextInput(attrs={'placeholder': 'Eg. Nature', 'class': 'form-control'}),
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Images
        fields = ['title', 'image', 'tag']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'title', 'class': 'form-control'}),
            'image': forms.FileInput(),
            'tag': forms.SelectMultiple(attrs={'class': 'multiple form-control bg-dark text-white'}),
        }
