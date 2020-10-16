from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone
from django.urls import reverse
from django.apps import apps

GENDER = (
    ('FEMALE','FEMALE'),
    ('MALE', 'MALE'),
)


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=200, help_text="Enter a book Category (e.g. Science, Poetry etc.)")
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name=models.CharField(max_length=100,blank=True,null=True)
    date_of_birth = models.DateField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'Author: ' + self.first_name + ' ' + self.last_name

    def __str__(self):
        return 'Author: ' + self.first_name + ' ' + self.last_name

    class Meta:
        get_latest_by = "first_name"
        ordering = ['last_name', 'last_name']
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author,help_text="Select an Author from the list",on_delete=models.CASCADE, related_name='authorsofbook')
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    category = models.ForeignKey(Category, help_text="Select a Category for this book",on_delete=models.CASCADE, related_name='categoriesofbook')
    quantity_total_copies = models.IntegerField(default=1)
    #available_copies = models.IntegerField()
    #pictureofbook=models.ImageField(blank=True, null=True, upload_to='book_image')
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

class Borrower(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE,related_name='borrowerstudent')
    book = models.ForeignKey('Book', on_delete=models.CASCADE,related_name='borrowerbook')
    issue_date = models.DateTimeField(null=True,blank=True)
    return_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.student.user.first_name+self.student.user.last_name+" borrowed "+self.book.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nu_id = models.CharField(max_length=10,unique=True)
    department = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, blank=True, choices=GENDER)
    #total_books_due=models.IntegerField(default=0)
    #email=models.EmailField(unique=True)
    #pic=models.ImageField(blank=True, upload_to='profile_image')
    age = models.IntegerField('Age', blank=True, null=True)
    dob = models.DateField('Date of Birth', blank=True, null=True)
    street = models.CharField('Street', max_length=200, blank=True, null=True)
    city = models.CharField('City', max_length=50, blank=True, null=True)
    state = models.CharField('State', max_length=50, blank=True, null=True)
    zipcode = models.CharField('Zip Code', max_length=10, blank=True, null=True)
    created_date = models.DateTimeField('Created Date', default=timezone.now)
    updated_date = models.DateTimeField('Updated Date', auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nu_id

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, blank=True, choices=GENDER)
    age = models.IntegerField('Age', blank=True, null=True)
    dob = models.DateField('Date of Birth', blank=True, null=True)
    street = models.CharField('Street', max_length=200, blank=True, null=True)
    city = models.CharField('City', max_length=50, blank=True, null=True)
    state = models.CharField('State', max_length=50, blank=True, null=True)
    zipcode = models.CharField('Zip Code', max_length=10, blank=True, null=True)
    created_date = models.DateTimeField('Created Date', default=timezone.now)
    updated_date = models.DateTimeField('Updated Date', auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.user)




