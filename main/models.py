from django.db import models
class  book(models.Model):

    book_id = models.CharField(max_length=30)
    title =  models.CharField(max_length=30)
    author =  models.CharField(max_length=30)
    genre =  models.CharField(max_length=30)
    status = models.CharField(max_length=50,default = "Available")

class issuebook_model(models.Model):
    book_id = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    issued_to = models.CharField(max_length=30)
    issue_date = models.CharField(max_length=30)
    return_date = models.CharField(max_length=30)

class student(models.Model):
    library_id = models.CharField( max_length=50)
    name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=50)
    email_id = models.CharField(max_length=50)
    course = models.CharField(max_length=50 )
