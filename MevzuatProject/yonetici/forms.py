from django import forms




class LoginForm(forms.Form):
    username1 = forms.CharField(label="Kullanıcı Adı")
    password1 = forms.CharField(label="Parola", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username1 = forms.CharField(max_length=50, label="Kullanıcı Adı")
    password1 = forms.CharField(max_length=20, label="Parola", widget=forms.PasswordInput)
    confirm1 = forms.CharField(max_length=20, label="Parolayı Doğrula", widget=forms.PasswordInput)

    def clean(self):
        username1 = self.cleaned_data.get("username1")
        password1 = self.cleaned_data.get("password1")
        confirm1 = self.cleaned_data.get("confirm1")

        if password1 and confirm1 and password1 != confirm1:
            raise forms.ValidationError("Parolalar Eşleşmiyor")

        values = {
            "username": username1,
            "password": password1
        }
        return values


