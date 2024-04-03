from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, GroupChat

class ProfileEditForm(forms.ModelForm):
    new_username = forms.CharField(max_length=150, required=False, label='Новый никнейм')

    class Meta:
        model = UserProfile
        fields = ['avatar', 'status', 'new_username']

class ChatForm(forms.ModelForm):
    class Meta:
        model = GroupChat
        fields = ['name', 'members']