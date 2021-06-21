from django.contrib import admin
from.models import book,student,issuebook_model

# Register your models here.
#admin.site.register(issued_book)
class bookAdmin(admin.ModelAdmin):
     list_display =  ['id','book_id','title','author','genre','status']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','library_id','name','phone_no','email_id','course',]

class IssuebookAdmin(admin.ModelAdmin):
    list_display = ['book_id','title','issued_to','issue_date','return_date']

admin.site.register(book,bookAdmin)
admin.site.register(student,StudentAdmin)
admin.site.register(issuebook_model,IssuebookAdmin)



