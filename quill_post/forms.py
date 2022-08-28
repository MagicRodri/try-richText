from django import forms
from .models import QPost

class QPostForm(forms.ModelForm):
    
    class Meta:
        model = QPost
        fields = ("content",)
