from django.db import models

# Create your models here.
class Student(models.Model):
	tzid=models.CharField(max_length=20,primary_key=True)
	sname=models.CharField(max_length=100)
	gender=models.CharField(max_length=10)
	contact=models.CharField(max_length=15);
	email=models.CharField(max_length=40)
	institute=models.CharField(max_length=100)
	address=models.CharField(max_length=200)
	
class Stdent(models.Model):
	tzid=models.ForeignKey(Student,null=False,on_delete=models.CASCADE)
	roomNo=models.CharField(max_length=10)
	
	
	
class Room(models.Model):
	roomNo=models.CharField(max_length=30,primary_key=True)
	floorNo=models.IntegerField()
	blkid=models.IntegerField()
	capacity=models.IntegerField()
	availability=models.IntegerField()
	
		

    	
	
