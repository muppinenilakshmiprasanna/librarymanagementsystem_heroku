from django.conf.urls import url
from . import views
from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'lms'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('aboutus', views.aboutus,name='aboutus'),

    path('adminclick', views.adminclick,name='adminclick'),
    path('studentlink', views.studentlink,name='studentlink'),

    path('adminsignup', views.adminsignupview,name='adminsignup'),
    path('adminlogin', LoginView.as_view(template_name='lms/adminlogin.html'), name='adminlogin'),

    path('studentsignup', views.studentsignupview,name='studentsignup'),
    path('studentlogin', LoginView.as_view(template_name='lms/studentlogin.html'),name='studentlogin'),

    path('afterlogin', views.afterloginview,name='afterlogin'),
    #urls for category
    path('category/new/', views.category_new, name='category_new'),
    path('category/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('category/<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('category_list', views.category_list, name='category_list'),
    #urls for author
    path('author/new/', views.author_new, name='author_new'),
    path('author/<int:pk>/edit/', views.author_edit, name='author_edit'),
    path('author/<int:pk>/delete/', views.author_delete, name='author_delete'),
    path('author_list', views.author_list, name='author_list'),
    #urls for book
    path('book/new/', views.book_new, name='book_new'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('book_list', views.book_list, name='book_list'),

    path('issuebook', views.issuebook, name='issuebook'),
    path('view/issuedbook', views.viewissuedbooks, name='viewissuedbooks'),
    path('returnbook/<int:pk>', views.returnbook, name='returnbook'),

    path('viewstudent', views.viewstudent,name='viewstudent'),

    path('staff_profile', views.staff_profile, name='staff_profile'),
    path('staff_profile_edit/<int:pk>', views.staff_profile_edit, name='staff_profile_edit'),
    path('admin_profile_edit/<int:pk>', views.admin_profile_edit, name='admin_profile_edit'),

    path('student_profile', views.student_profile, name='student_profile'),
    path('student_profile_edit/<int:pk>', views.student_profile_edit, name='student_profile_edit'),

    path('view/issuebookstostudent', views.viewissuedbookstostudent, name='viewissuedbookstostudent'),
    url(r'^contactus/$', views.contactus, name='contactus'),
    path('contactussuccess', views.contactussuccess,name='contactussuccess'),





]













