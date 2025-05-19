from django import forms
from .models import document, comment

class create_blog(forms.ModelForm):
    name = forms.CharField(required=1, label="Tên tài liệu")
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols" : 30}), required=True, label="Mô tả")
    file = forms.FileField(label="Tài liệu")
    class Meta:
        model = document
        fields = [
            'name',
            'description',
            'file',

        ]
    def clean_create_blog(self, *args, **kargs):
        blog = self.cleaned_data.get("create_blog")
        return blog
    
class create_comment(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows": 2, "cols" : 30}), required=True, label="Mô tả")
    class Meta:
        model = comment
        fields = [
            'content',
        ]
    def clean_create_blog(self, *args, **kargs):
        blog = self.cleaned_data.get("create_blog")
        return blog