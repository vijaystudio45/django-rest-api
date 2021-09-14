from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Student
# Create your views here.

@api_view(['GET'])
def student_list(request):
	student = Student.objects.all().order_by('-id')
	serializer = TaskSerializer(student, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def student_create(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response("Student data Created Successfully")

@api_view(['POST'])
def student_update(request):
	id = request.data['id']
	if Student.objects.filter(id=id).exists():
		student = Student.objects.get(id=id)
		serializer = TaskSerializer(instance=student, data=request.data)

		if serializer.is_valid():
			serializer.save()

		return Response("student data updated successfully")
	else:
		return Response("student id not exists in database.")


@api_view(['POST'])
def student_delete(request):
	id=request.data['id']
	if Student.objects.filter(id=id).exists():
		student = Student.objects.get(id=id)
		student.delete()
		return Response('Item successfully delete!')
	else:
		return Response("student id not exists in database.")



