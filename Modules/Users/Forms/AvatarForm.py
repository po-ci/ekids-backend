from django import forms
from ..Models.Avatar import Avatar
from django.core import validators


class AvatarForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Avatar
        fields = ('image',)
