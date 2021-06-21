from django.shortcuts import render
from .models import book,student,issuebook_model
from .serializers import bookSerializer,studentSerializer,issuebookSerializer
from django.contrib import messages
from django.http import Http404
#========================= rest api imports====================

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

#=================================  API code for Book ====================                                                                      
class book_List(APIView):
    def get(self,request):
        books = book.objects.all()
        serializer = bookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self,request):
        print(request.data)
        serializer = bookSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class book_Detail(APIView):
    def get_object(self,pk):
        try:
            Book =  book.objects.get(pk = pk)
            return Book
        except book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Book =  book.objects.get(pk = pk)
        serializer = bookSerializer(Book)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        object_book = self.get_object(pk)
        serializer = bookSerializer(object_book, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        object_book = self.get_object(pk)
        object_book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


 
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(book_Detail, self).dispatch(*args, **kwargs)
    
#================== Api code for Student  ===============================
class student_List(APIView):

    def get(self,request):
        students = student.objects.all()
        serializer =   studentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self,request):
        print(request.data)
        serializer = studentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class student_Detail(APIView):
    """
    Retrieve, update or delete a code student.
    """
    def get_object(self,pk):
        try:
            object_student =  student.objects.get(pk = pk)
            return object_student
        except student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        object_student =  student.objects.get(pk = pk)
        serializer = studentSerializer(object_student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        object_student = self.get_object(pk)
        print(object_student)
        print(request.data)
        serializer = studentSerializer(object_student, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        object_student = self.get_object(pk)
        object_student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


 
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(student_Detail, self).dispatch(*args, **kwargs)

#============================== API for Issue/Return Book====================
class Issue_Book_API(APIView):
    def get(self,request):
        issued_book_obj = issuebook_model.objects.all() 
        serializer = issuebookSerializer(issued_book_obj, many=True)
        return Response(serializer.data)

    def post(self,request):
        print(request.data)
        serializer = issuebookSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Issue_Book_Detail_API(APIView):

    def get_object(self,pk):
        try:
            issued_book_obj = issuebook_model.objects.get(pk=pk) 
            return issued_book_obj
        except  issuebook_model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        issued_book_obj = issuebook_model.objects.get(pk=pk)
        serializer = issuebookSerializer(issued_book_obj)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        issued_book_obj = issuebook_model.objects.get(pk=pk)
        issued_book_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#=============================== rendering templates  ===============================
class Homeview(APIView):
    pass

def home(request):
    return render(request,'Home.html')
def view_book(request):
    books = book.objects.all()
    return render(request,'ViewBooks.html',{'books':books})

def add_book(request):
    return render(request,'AddBook.html')

def delete_book(request):
    return render(request,'DeleteBook.html')

def update_book(request,pk):
    books = book.objects.get(pk =pk)
    return render(request,'UpdateBook.html',{'books':books})

def delete_book(request,pk):
    books = book.objects.get(pk =pk)
    return render(request,'DeleteBook.html',{'books':books})

def view_student(request):
    students = student.objects.all()
    return render(request,'Viewstudent.html',{'students':students})

def add_student(request):
    return render(request,'AddStudent.html')

def update_student(request,pk):
    students = student.objects.get(pk =pk)
    return render(request,'UpdateStudent.html',{'students':students})

def delete_student(request,pk):
    students = student.objects.get(pk =pk)
    return render(request,'DeleteStudent.html',{'students':students})

def available_book(request):
    object_books = book.objects.filter(status = "Available")
    return render(request,'Available_book.html',{'books':object_books,})

def issue_book(request,pk):
    books = book.objects.get(pk =pk)
    students = student.objects.all()
    return render(request,'Issue_book.html',{'books':books,'students':students})

def issued_book(request):
    issued_book_obj = issuebook_model.objects.all() 
    return render(request,'Issued_book.html',{'issued_books':issued_book_obj,})

def return_book(request,pk):
    issued_book_obj = issuebook_model.objects.get(pk = pk)
    if request.method == 'POST':
        book_id = request.POST['book_id']
        print("book id",book_id)
        status = request.POST['status']
        print("stautus",status)
        books = book.objects.all()
        book.objects.filter(book_id = book_id).update(status =  status )

    return render(request,'ReturnBook.html',{'issued_books':issued_book_obj,})