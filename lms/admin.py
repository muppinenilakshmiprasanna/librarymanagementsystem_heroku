from django.contrib import admin

# Register your models here.
from .models import Borrower, Category, Author, Book, Staff, Student


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date', 'updated_date', ]
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ['name', 'created_date']


admin.site.register(Category,CategoryAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','created_date' ]
    list_filter = ('created_date',)
    search_fields = ('first_name','last_name')
    ordering = ['first_name','last_name', 'created_date']


admin.site.register(Author,AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'isbn', 'author','category', ]
    list_filter = ('category','author')
    search_fields = ('name','isbn')
    ordering = ['name','author', 'category']


admin.site.register(Book,BookAdmin)


class BorrowerAdmin(admin.ModelAdmin):
    list_display = ['student', 'book', 'issue_date','return_date', ]
    list_filter = ('student','book')
    search_fields = ('student','book')
    ordering = ['student','book',]

admin.site.register(Borrower,BorrowerAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('nu_id', 'user','department', 'phone_number')
    list_filter = ('department',)
    search_fields = ('nu_id',)
    ordering = ['user','nu_id']

admin.site.register(Student, StudentAdmin)


class StaffAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'phone_number')
    search_fields = ('user',)
    ordering = ['user', ]


admin.site.register(Staff, StaffAdmin)