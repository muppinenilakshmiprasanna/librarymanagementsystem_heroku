"""libraryms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path, include, re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lms.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('', include('django.contrib.auth.urls')),
    path('logout', LogoutView.as_view(template_name='registration/logout.html'),name='logout'),

    re_path(r'^accounts/password/reset/$',
            PasswordResetView.as_view(template_name='registration/password_reset_page.html'), name='password_reset'),
    re_path(r'^accounts/password/reset/done/$',
            PasswordResetDoneView.as_view(template_name='registration/passwordreset_pagedone.html'),
            name='password_reset_done'),
    re_path(r'^accounts/password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
            PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirmpage.html'),
            name='password_reset_confirm'),
    re_path(r'^accounts/password/reset/complete/$',
            PasswordResetCompleteView.as_view(template_name='registration/password_reset_completepage.html'),
            name='password_reset_complete'),

    re_path(r'^accounts/password/change/$',
            PasswordChangeView.as_view(template_name='registration/change-password.html'), name='password_change'),
    re_path(r'^accounts/password/change/done/$',
            PasswordChangeDoneView.as_view(template_name='registration/change-password-done.html'),
            name='password_change_done'),


]
