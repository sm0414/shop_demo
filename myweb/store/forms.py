from django import forms
from .models import Customer


class LoginForm(forms.Form):
    userid = forms.CharField(label='帳號：', required=True)
    password = forms.CharField(label='密碼：', widget=forms.PasswordInput)


class RegistrationForm(forms.Form):
    userid = forms.CharField(label='帳號：', required=True)
    name = forms.CharField(label='姓名：', required=True)
    password1 = forms.CharField(label='密碼：', widget=forms.PasswordInput)
    password2 = forms.CharField(label='再次輸入密碼：', widget=forms.PasswordInput)
    birthday = forms.DateField(label='生日：', required=True, error_messages={'invalid': '輸入的生日格式錯誤'})
    address = forms.CharField(label='通讯地址：', required=True)
    phone = forms.CharField(label='电话号码：', required=True)
    
    def clean_userid(self):
        userid = self.cleaned_data.get('userid')
        c = Customer.objects.filter(userid=userid)
        if len(c) > 0:
            raise forms.ValidationError('帳號已存在')
            
        return userid
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('密碼輸入不一致')

        return password2
