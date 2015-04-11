from blogsite.models import BlogPost,Comment
from django import forms

class newBlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost

class newCommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['name', 'body',]
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Name'}),
            'body' : forms.Textarea(attrs={'class': 'form-control', 'rows': 2,
                                           'placeholder': 'Comment Here'}),
            #'post' : forms.ModelChoiceField(queryset=BlogPost.objects.all(), to_field_name='post'),
            }