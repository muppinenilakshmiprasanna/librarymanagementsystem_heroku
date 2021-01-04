from django.contrib import admin

# Register your models here.
from django.http import HttpResponse

from .models import Borrower, Category, Author, Book, Staff, Student
import csv


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response
    export_as_csv.short_description = "Export Selected AS CSV"


class CategoryAdmin(admin.ModelAdmin,ExportCsvMixin):
    list_display = ['name', 'created_date', 'updated_date', ]
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ['name', 'created_date']
    actions = ["export_as_csv"]


admin.site.register(Category,CategoryAdmin)


class AuthorAdmin(admin.ModelAdmin,ExportCsvMixin):
    list_display = ['first_name', 'last_name','created_date' ]
    list_filter = ('created_date',)
    search_fields = ('first_name','last_name')
    ordering = ['first_name','last_name', 'created_date']
    actions = ["export_as_csv"]


admin.site.register(Author,AuthorAdmin)


class BookAdmin(admin.ModelAdmin,ExportCsvMixin):
    list_display = ['name', 'isbn', 'author','category', ]
    list_filter = ('category','author')
    search_fields = ('name','isbn')
    ordering = ['name','author', 'category']
    actions = ["export_as_csv"]


admin.site.register(Book,BookAdmin)


class BorrowerAdmin(admin.ModelAdmin,ExportCsvMixin):
    list_display = ['student','book','issue_date','excepted_return_date','actual_return_date','created_date', 'updated_date', ]
    list_filter = ('student','book')
    search_fields = ('student','book')
    ordering = ['student','book',]
    actions = ["export_as_csv"]


admin.site.register(Borrower,BorrowerAdmin)


class StudentAdmin(admin.ModelAdmin,ExportCsvMixin):
    list_display = ('nu_id', 'user','department', 'phone_number')
    list_filter = ('department',)
    search_fields = ('nu_id',)
    ordering = ['user','nu_id']
    actions = ["export_as_csv"]


admin.site.register(Student, StudentAdmin)


class StaffAdmin(admin.ModelAdmin,ExportCsvMixin):
    list_display = ( 'user', 'phone_number')
    search_fields = ('user',)
    ordering = ['user', ]
    actions = ["export_as_csv"]


admin.site.register(Staff, StaffAdmin)