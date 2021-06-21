from django.contrib import admin
from django.urls import path, include
from main.views import Homeview
from main import views
from rest_framework.urlpatterns import format_suffix_patterns

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('viewbook/',views.view_book),
    path('addbook/',views.add_book),
    path('deletebook/',views.delete_book),

    path('viewbook/updatebook/<int:pk>/',views.update_book),
    path ('viewbook/deletebook/<int:pk>/',views.delete_book),
#==========================API Urls======================    
    path('books/', views.book_List.as_view(),name = "Books List"),
    path('books/<int:pk>/', csrf_exempt(views.book_Detail.as_view()),name = "Book Details API VIEW"),
#========================Student API Urls =====================
    path('students/', views.student_List.as_view()),
    path('students/<int:pk>/', views.student_Detail.as_view()),
#===================================
    path('studentdetails/',views.view_student),
    path('addstudent/',views.add_student),
    path('studentdetails/updatestudent/<int:pk>/',views.update_student),
    path ('studentdetails/deletestudent/<int:pk>/',views.delete_student),

#==================issue/return==================
    path('issuebook/<int:pk>/',views.issue_book),
    path('returnbook/<slug:pk>/',views.return_book),

    path('availablebook/',views.available_book),
    path('issuedbook/',views.issued_book),
#========================Student API Urls =====================
    path('API/issuebook/', views.Issue_Book_API.as_view(),name = "issue/return list"),
    path('API/issuebook/<int:pk>/',views.Issue_Book_Detail_API.as_view(),name = "issue/return Details List"),
    #path('students/<int:pk>/', views.student_Detail.as_view

]

urlpatterns = format_suffix_patterns(urlpatterns)