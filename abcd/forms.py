from django import forms
from abcd.models import Todo
from abcd.models import UserProfile
from django.contrib.auth.forms import UserCreationForm


class Todoform(forms.ModelForm):
    class Meta:
        model = Todo
        fields = [ 'task', 'description', 'cataegory' ,'time', 'due_on']


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields = [
                  "username",
                  "full_name",
                  "email",
                  "password1",
                  "password2"
                  ]



    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['full_name']
        if commit:
            user.save()
        return user