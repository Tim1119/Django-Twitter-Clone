from .models import Post,Comment,Profile
from django import forms
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = '__all__'

class EditProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = '__all__'


   