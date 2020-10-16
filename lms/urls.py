from django.conf.urls import url
from django.contrib.auth.views import LogoutView, LoginView

from . import views
from django.urls import path, re_path

app_name = 'lms'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    #path('logout', LogoutView.as_view(template_name='library/index.html')),
    #path('afterlogin', views.afterlogin_view,name='afterlogin'),
    #path('aboutus', views.aboutus_view,name='aboutus'),
    #path('adminclick', views.adminclick_view,name='adminclick'),
    #path('studentclick', views.studentclick_view,name='studentclick'),
    #path('adminsignup', views.adminsignup_view,name='adminsignup'),
    #path('adminlogin', LoginView.as_view(template_name='library/adminlogin.html'),name='adminlogin'),
    #path('studentsignup', views.studentsignup_view,name='studentsignup'),
    #path('studentlogin', LoginView.as_view(template_name='library/studentlogin.html'),name='studentlogin'),

]













