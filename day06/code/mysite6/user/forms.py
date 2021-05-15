from django import forms


class MyRegFrom(forms.Form):
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密码')
    password2 = forms.CharField(label='重复秘密')

    def clean_username(self):
        uname = self.cleaned_data['username']
        if len(uname) <= 3:
            raise forms.ValidationError('用户名太短')
        return uname
