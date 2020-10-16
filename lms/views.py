from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .models import Book
def home(request):
    return render(request,'lms/index.html')


"""def BookListView(request):
    book_list = Book.objects.all()
    # MODELNAME.objects.all() is used to get all objects i.e. tuples from database
    return render(request, 'lms/book_list.html', {'books': book_list})



def is_student(user):
    return user.groups.filter(name='Student').exists()


def afterlogin_view(request):
    if is_student(request.user):
        return render(request,'lms/studentafterlogin.html')
    else:
        return render(request,'lms/staffafterlogin.html')
"""

"""#for showing signup/login button for student
def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'lms/studentclick.html')

#for showing signup/login button for staff
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'lms/adminclick.html')"""