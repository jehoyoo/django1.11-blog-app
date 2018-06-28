#ModelForm을 상속받는 PostModelForm클래스
from django import forms
from .models import Post

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text')
