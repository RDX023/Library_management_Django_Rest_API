from rest_framework import serializers
from .models import  book,student,issuebook_model

class  bookSerializer(serializers.ModelSerializer):
	class Meta:
		model = book
		fields = ['id','book_id','title','author','genre','status']


class studentSerializer(serializers.ModelSerializer):
	class Meta:
		model = student
		fields = ['id','library_id','name','phone_no','email_id','course',]

class issuebookSerializer(serializers.ModelSerializer):
	class Meta:
		model = issuebook_model
		fields = ['id','book_id','title','issued_to','issue_date','return_date']