from django import forms
from .models import document, comment
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
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
    
class register(forms.ModelForm):
    username = forms.CharField(label="Tên đăng nhập ")
    password = forms.CharField(label= "Mật khẩu", widget=forms.PasswordInput)
    password_confirm = forms.CharField(label= "Xác nhận mật khẩu", widget=forms.PasswordInput)
    # email = forms.EmailField(validators=[EmailValidator(message="Vui lòng nhập một địa chỉ email hợp lệ.")], label='email')
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password_confirm',
            # 'email'
        ]
    def clean(self): #định nghĩa data được clean như thế nào (validate)
        clean_data = super().clean()
        password = clean_data.get('password')
        password_confirm = clean_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Mật khẩu xác nhận không khớp !!')
        return clean_data
    def clean_username(self, *args, **kargs):
        username = self.cleaned_data.get('username') 
        if User.objects.filter(username=username).exists():
            raise ValidationError('username đã được sử dụng!!')
        return username
    # def clean_email(self, *args, **kargs):
    #     email = self.cleaned_data.get('email') 
    #     if User.objects.filter(email = email).exists():
    #         raise ValidationError('email đã được sử dụng!!')
    #     return email
