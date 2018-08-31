from django import forms
from .models import User, Group, Posts, Pictures
from django.contrib.auth import password_validation


class Register_form(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput({'placeholder': 'Enter username', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput({'placeholder': 'Enter email', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Enter password', 'class': 'form-control'}), validators=[password_validation.validate_password])
    password_confirmation = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Confirm password', 'class': 'form-control'}))

    class Meta():
        model = User
        fields = ['username', 'email', 'password', 'password_confirmation']

    def clean_password_confirmation(self):
        all_clean_data = super().clean()
        try:
            password = all_clean_data['password']
            password_confirmation = all_clean_data['password_confirmation']
        except KeyError:
            pass
        else:
            if password != password_confirmation:
                raise forms.ValidationError('Passwords do not match')


class Login_form(forms.Form):
    username = forms.CharField(widget=forms.TextInput({'placeholder': 'Enter username', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Enter password', 'class': 'form-control'}))


class Group_form(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput({'placeholder': 'Enter title', 'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea({'placeholder': 'Enter description', 'class': 'form-control', 'rows': 3}))

    class Meta():
        model = Group
        fields = ['title', 'description']


def get_groups():
    'Uzima grupe koje postoje'
    CHOICES = [(i.id, i.title) for i in Group.objects.all()]
    return CHOICES


class Post_form(forms.ModelForm):
    """ Da ubaci user-a u formu, ali ne vidim primenu!!!!

    def __init__(self, user, *args, **kwargs):
        self.current_user = user
        super(Post_form, self).__init__(*args, **kwargs)
    """
    choose_group = forms.ChoiceField(widget=forms.Select({'class': 'form-control'}), choices=get_groups) # pomocno polje jer treba da se upise Group object a iz liste izbora ne moze da se prenese objekat!!!
    text = forms.CharField(widget=forms.Textarea({'placeholder': 'Enter text', 'class': 'form-control', 'rows': 3}))

    class Meta():
        model = Posts
        fields = ['choose_group', 'text']


class Post_form_within_group(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea({'placeholder': 'Enter text', 'class': 'form-control', 'rows': 3}))

    class Meta():
        model = Posts
        fields = ['text']


class Pictures_form(forms.ModelForm):
    picture = forms.ImageField(label='Upload picture')

    class Meta():
        model = Pictures
        fields = ['picture']