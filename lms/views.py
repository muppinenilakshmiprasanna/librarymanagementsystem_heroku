import csv

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from . import forms,models
from django.contrib.auth.models import Group, User
from django.contrib import auth
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.core.mail import send_mail
from libraryms.settings import EMAIL_HOST_USER
from .forms import RegisterForm, StaffSignUpForm, StudentSignUpForm, CategoryForm, AuthorForm, BookForm, IssueBookForm, \
    ReturnBookForm, StaffProfileEditForm, StudentProfileEditForm, AdminProfileEditForm
from .models import Category, Author, Book, Borrower, Student, Staff


def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'lms/home.html', {'lms': home})

def aboutus(request):
    return render(request, 'lms/aboutus.html', {'lms': aboutus})


def contactus(request):
    if request.method == 'POST':
        form = forms.ContactusForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Email']
            name=form.cleaned_data['Name']
            message = form.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message, EMAIL_HOST_USER, ['lakshmiprasanna.muppineni26@gmail.com'], fail_silently = False)
        return redirect('lms:contactussuccess')
    else:
        form = forms.ContactusForm()
    return render(request, 'lms/contactus.html', {'form': form})


def contactussuccess(request):
    return render(request, 'lms/contactsuccess.html')


# signup/login button for student
def studentlink(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'lms/studentclick.html')

#signup/login button for staff
def adminclick(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'lms/adminclick.html')


def is_student(user):
    return user.groups.filter(name='STUDENT').exists()


def afterloginview(request):
    if is_student(request.user):
        return render(request,'lms/studentafterlogin.html')
    else:
        return render(request,'lms/adminafterlogin.html')


def adminsignupview(request):
    print("in admin signup")
    if request.method == 'POST':
        print("in admin signup in post")
        userform = RegisterForm(request.POST, prefix='adminregisterform')
        staffform = StaffSignUpForm(request.POST, prefix='staffregisterform')
        if userform.is_valid() and staffform.is_valid():
            user = userform.save()
            user.is_staff = True
            user.save()
            print(user)
            print("before staff page")
            staff = staffform.save(commit=False)
            staff.user = user
            staff.save()
            print(staff.user)
            my_admin_group = Group.objects.get_or_create(name='STAFF')
            my_admin_group[0].user_set.add(user)
            print(my_admin_group[0])
        return HttpResponseRedirect(reverse('lms:adminlogin'))
    else:
        print("in admin signup not post")
        userform = RegisterForm(prefix='adminregisterform')
        staffform = StaffSignUpForm(request.POST, prefix='staffregisterform')
    return render(request, 'lms/adminsignup.html',{'userform': userform, 'staffform': staffform})

def studentsignupview(request):
    if request.method == 'POST':
        userform = RegisterForm(request.POST, prefix='studentregisterform')
        studentform = StudentSignUpForm(request.POST, prefix='studentextraregisterform')
        if userform.is_valid() and studentform.is_valid():
            user = userform.save()
            user.save()
            student = studentform.save(commit=False)
            student.user = user
            student.save()
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        return HttpResponseRedirect(reverse('lms:studentlogin'))
    else:
        userform = RegisterForm(prefix='studentregisterform')
        studentform = StudentSignUpForm(request.POST, prefix='studentextraregisterform')
    return render(request, 'lms/studentsignup.html',{'userform': userform, 'studentform': studentform})


@login_required
def category_list(request):
    categories = Category.objects.filter(created_date__lte=timezone.now())
    return render(request, 'lms/category_list.html', {'categories': categories})

@login_required()
def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.created_date = timezone.now()
            category.save()
            return redirect('lms:category_list')
    else:
        form = CategoryForm()
        # print("Else")
    return render(request, 'lms/category_new.html', {'form': form})


@login_required()
def category_edit(request,pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            category.updated_date = timezone.now()
            category.save()
            return redirect('lms:category_list')
    else:
        # print("else")
        form = CategoryForm(instance=category)
    return render(request, 'lms/category_edit.html', {'form': form})


@login_required()
def category_delete(request, pk):
    product = get_object_or_404(Category, pk=pk)
    product.delete()
    return redirect('lms:category_list')


@login_required
def author_list(request):
    authors = Author.objects.filter(created_date__lte=timezone.now())
    return render(request, 'lms/author_list.html', {'authors': authors})

@login_required()
def author_new(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.created_date = timezone.now()
            author.save()
            return redirect('lms:author_list')
    else:
        form = AuthorForm()
        # print("Else")
    return render(request, 'lms/author_new.html', {'form': form})


@login_required()
def author_edit(request,pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            author = form.save()
            author.updated_date = timezone.now()
            author.save()
            return redirect('lms:author_list')
    else:
        # print("else")
        form = AuthorForm(instance=author)
    return render(request, 'lms/author_edit.html', {'form': form})


@login_required()
def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author.delete()
    return redirect('lms:author_list')


@login_required
def book_list(request):
    books = Book.objects.filter(created_date__lte=timezone.now())
    return render(request, 'lms/book_list.html', {'books': books})

@login_required()
def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.created_date = timezone.now()
            book.save()
            return redirect('lms:book_list')
    else:
        form = BookForm()
        # print("Else")
    return render(request, 'lms/book_new.html', {'form': form})


@login_required()
def book_edit(request,pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            book.updated_date = timezone.now()
            book.save()
            return redirect('lms:book_list')
    else:
        # print("else")
        form = BookForm(instance=book)
    return render(request, 'lms/book_edit.html', {'form': form})


@login_required()
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('lms:book_list')

@login_required()
def issuebook(request):
    books = Book.objects.filter(quantity_total_copies__gt=0)
    print("books",books)
    if request.method == "POST":
        print("opening new form request method is post")
        form = IssueBookForm(request.POST)
        print("opening new form request method is post and before if method")
        if form.is_valid():
            print("opening new form request method is post and after if method")
            borrower = form.save(commit=False)
            book=borrower.book
            print(borrower.excepted_return_date)
            print(borrower.issue_date)
            print(book.quantity_total_copies)
            book.quantity_total_copies = book.quantity_total_copies - 1
            book.updated_date = timezone.now()
            book.save()
            borrower.excepted_return_date = borrower.issue_date+timedelta(days=15)
            print(borrower.excepted_return_date)
            borrower.created_date = timezone.now()
            borrower.save()
            print(book.quantity_total_copies)
            return render(request, 'lms/book_issued.html')
    else:
        print("opening new form1")
        form = IssueBookForm()
        form.fields['book'].queryset = books
    return render(request, 'lms/issuebook.html', {'form': form})


@login_required()
def returnbook(request,pk):
    borrower = get_object_or_404(Borrower, pk=pk)
    print(borrower)
    book=get_object_or_404(Book,pk=borrower.book.pk)
    print(book)
    if request.method == "POST":
        form =ReturnBookForm(request.POST, instance=borrower)
        if form.is_valid():
            borrower = form.save(commit=False)
            book.quantity_total_copies = book.quantity_total_copies + 1
            book.updated_date = timezone.now()
            book.save()
            borrower.updated_date = timezone.now()
            borrower.save()
            print(book.quantity_total_copies)
            return redirect('lms:viewissuedbooks')
    else:
        print("else")
        form = ReturnBookForm(instance=borrower)
    return render(request, 'lms/returnbook.html', {'form': form})

@login_required()
def viewissuedbooks(request):
    issuedbooks=Borrower.objects.filter(created_date__lte=timezone.now())
    return render(request,'lms/viewissuedbook.html',{'issuedbooks':issuedbooks})


@login_required(login_url='studentlogin')
def viewissuedbookstostudent(request):
    student = Student.objects.get(user_id=request.user.id)
    print(student)
    issuedbooks = Borrower.objects.filter(student_id=student.pk)
    print(issuedbooks)
    return render(request,'lms/viewissuedbookbystudent.html',{'issuedbooks':issuedbooks})

@login_required()
def viewstudent(request):
    students = Student.objects.all()
    return render(request,'lms/viewstudent.html',{'students': students})

@login_required()
def staff_profile(request):
    print("User:" + str(request.user))
    print(request.path)
    print(request.user.id)
    if request.user.is_superuser:
        user = User.objects.get(id=request.user.id)
        print("user details", user)
        return render(request, 'lms/superuserprofile.html', {'user': user})
    else:
        staff = Staff.objects.get(user_id=request.user.id)
        print("staff details", staff)
    return render(request, 'lms/staffprofile.html', {'staff': staff})



@login_required()
def staff_profile_edit(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    user = get_object_or_404(User, pk=request.user.id)
    if request.method == "POST":
        staffform = StaffProfileEditForm(request.POST, instance=staff)
        userform = AdminProfileEditForm(request.POST, instance=user)
        if userform.is_valid() and staffform.is_valid():
            staff = staffform.save(commit=False)
            user = userform.save(commit=False)
            user.save()
            staff.user = user
            staff.updated_date = timezone.now()
            staff.save()
            return redirect('lms:staff_profile')
    else:
        staffform = StaffProfileEditForm(instance=staff)
        userform = AdminProfileEditForm(instance=user)
    return render(request, 'lms/staffprofile_edit.html', {'staffform': staffform,'userform':userform})

@login_required()
def admin_profile_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        # update
        form = AdminProfileEditForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.updated_date = timezone.now()
            user.save()
            return redirect('lms:staff_profile')
    else:
        # edit
        form = AdminProfileEditForm(instance=user)
    return render(request, 'lms/superuserprofileedit.html', {'form': form})



@login_required()
def student_profile(request):
    student = Student.objects.get(user_id=request.user.id)
    print("student details",student)
    return render(request, 'lms/studentprofile.html', {'student': student})


@login_required()
def student_profile_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    user = get_object_or_404(User, pk=request.user.id)
    if request.method == "POST":
        studentform = StudentProfileEditForm(request.POST, instance=student)
        userform = AdminProfileEditForm(request.POST, instance=user)
        if userform.is_valid() and studentform.is_valid():
            staff = studentform.save(commit=False)
            user = userform.save(commit=False)
            user.save()
            student.user = user
            student.updated_date = timezone.now()
            student.save()
            return redirect('lms:student_profile')
    else:
        studentform = StudentProfileEditForm(instance=student)
        userform = AdminProfileEditForm(instance=user)
    return render(request, 'lms/studentprofile_edit.html', {'studentform': studentform,'userform':userform})


"""def student_profile_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        # update
        form = StudentProfileEditForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.updated_date = timezone.now()
            student.save()
            #student = Student.objects.filter(pk=pk)
            #student = Student.objects.get(pk=pk)
            #print(student)
            #return render(request,'lms/studentprofile.html', {'student': student})
            return redirect('lms:student_profile')
    else:
        # edit
        form = StudentProfileEditForm(instance=student)
    return render(request, 'lms/studentprofile_edit.html', {'form': form})"""
