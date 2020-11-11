
from datetime import date, datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
from .models import Staff, Student, Author, Category, Book, Borrower


"""class DateInput(forms.DateInput):
    input_type = 'date'
    def __init__(self, **kwargs):
        kwargs["format"] = '%m/%d/%Y'
        super().__init__(**kwargs)"""


class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'password1', 'password2',)


class StaffSignUpForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('gender','age','dob','street', 'city' ,'state', 'zipcode', 'phone_number')
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date',},)
        }


class StudentSignUpForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('nu_id','department','gender','age','dob','street', 'city' ,'state', 'zipcode', 'phone_number')
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date', },)
        }


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('first_name','last_name','middle_name','date_of_birth')
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', },)
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name','author','isbn','category','quantity_total_copies')


class IssueBookForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ('student','book','issue_date',)
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date','min': datetime.today().strftime(format='%Y-%m-%d'),}),
            #'expected_return_date': forms.DateInput(),
        }

    def clean(self):
        cleaned_data = super(IssueBookForm, self).clean()
        issuedate = cleaned_data.get("issue_date")

        if issuedate :
            if datetime.today().date() < issuedate:
                raise forms.ValidationError("Issue date cannot be earlier than today's Date!")
        return cleaned_data

    """def __init__(self, *args, **kwargs):
        super(IssueBookForm, self).__init__(*args, **kwargs)
        self.fields['excepted_return_date'].disabled = True
        self.fields['excepted_return_date'].widget.format = '%m/%d/%Y'"""


class ReturnBookForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ('student','book','issue_date','excepted_return_date','actual_return_date',)
        widgets = {
            'issue_date': forms.DateInput(),
            'expected_return_date': forms.DateInput(),
            'actual_return_date': forms.DateInput(attrs={'class': 'date','type': 'date','placeholder': 'Select a date','min':datetime.today().strftime(format='%Y-%m-%d')})
        }

    def __init__(self, *args, **kwargs):
        super(ReturnBookForm, self).__init__(*args, **kwargs)
        self.fields['student'].disabled = True
        self.fields['book'].disabled = True
        self.fields['issue_date'].disabled = True
        self.fields['issue_date'].widget.format = '%m/%d/%Y'
        self.fields['excepted_return_date'].disabled = True
        self.fields['excepted_return_date'].widget.format = '%m/%d/%Y'

    def clean(self):
        cleaned_data = super(ReturnBookForm, self).clean()
        issuedate = cleaned_data.get("issue_date")
        actualreturndate = cleaned_data.get("actual_return_date")

        if issuedate and actualreturndate:
            if actualreturndate < issuedate:
                raise forms.ValidationError("Return date cannot be earlier than Issue Date!")
        return cleaned_data


class StaffProfileEditForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('age', 'dob', 'street','city', 'state','zipcode','gender','phone_number')
        widgets = {
            'dob': forms.DateInput(attrs={'class': 'datepicker','type': 'date',})
        }


class StudentProfileEditForm(forms.ModelForm):
    class Meta:
        model = Student
        #fields = ('user','age', 'dob', 'street','city', 'state','zipcode','gender','phone_number')
        fields = ('age', 'dob', 'street', 'city', 'state', 'zipcode', 'gender', 'phone_number')
        widgets = {
            'dob': forms.DateInput(attrs={'class': 'datepicker','type': 'date', },)
        }

    """def __init__(self, *args, **kwargs):
        super(StudentProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True"""


class AdminProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email', 'first_name', 'last_name',)

    def __init__(self, *args, **kwargs):
        super(AdminProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['username'].disabled = True