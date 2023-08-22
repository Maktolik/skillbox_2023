from django import forms
from django.contrib.auth.models import User

from myauth.models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar',)