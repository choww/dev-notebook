from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))

class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'input'}))
    password1 = forms.CharField(required=True,
                                label='Password', 
                                widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2 = forms.CharField(required=True,
                                label='Password confirmation',
                                widget=forms.PasswordInput(attrs={'class': 'input'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
        
    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)   
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class EditUserForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }

    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'input'}))

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={'class': 'input'}),
        required=False,
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label="New password confirmation",
        required=False,
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'input'}),
    )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 
                  'new_password1', 'new_password2')

    def clean_new_password2(self):  
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
            password_validation.validate_password(password2)
        return password2

    def save(self, commit=True):
        user = super(EditUserForm, self).save(commit=False)   
        password = self.cleaned_data["new_password1"]
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    bio = forms.CharField(label='Bio', 
                          required=False,
                          widget=forms.Textarea(attrs={'class': 'textarea'}))    
    location = forms.CharField(label='Location',
                               required=False,
                               widget=forms.TextInput(attrs={'class': 'input'}))
    photo = forms.ImageField(required=False)

    class Meta: 
        model = Profile
        fields = ('bio', 'location', 'photo')
    
    def save(self, user):
        user.profile.bio=self.cleaned_data['bio']
        user.profile.location=self.cleaned_data['location']
        user.profile.photo=self.cleaned_data['photo']
        user.profile.save()
