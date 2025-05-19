from django import forms
from .models import Comment
class Comment(forms.ModelForm):
    author = forms.CharField(required=True, label="author name")
    user_comment = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols" : 30}), required=True, label="User comment")
    class Meta:
        model = Comment
        fields = [
            'author',
            'user_comment'
        ]
    def clean_user_comment(self, *args, **kargs):
        comment = self.cleaned_data.get("user_comment")
        if "fuck" in comment:
            print('dit me may')
            raise forms.ValidationError("dit me may")
        return comment