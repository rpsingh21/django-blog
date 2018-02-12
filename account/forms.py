from django import forms

from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,
)

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    # doing forms vaildstions
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("User does not exist")

            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")

            if not user.is_active:
                raise forms.ValidationError("user is not active")
        return super(LoginForm, self).clean(*args, **kwargs)


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='conform password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Password does not matched !")
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        q_em = User.objects.filter(email=email)
        if q_em.exists():
            raise forms.ValidationError("Email alredy exist ")
        return email
