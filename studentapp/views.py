from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status

# View Batch
@api_view(['GET'])
def batch_list(request):
    if request.method == 'GET':
        category = Batch.objects.all()
        serializer = BatchSerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# View student list
@api_view(['GET'])
def student_list(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Add student 
@api_view(['GET','POST'])
def add_student(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Add batch 
@api_view(['GET','POST'])
def add_batch(request):
    if request.method == 'GET':
        batch = Batch.objects.all()
        serializer = BatchSerializer(batch, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = BatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Batch view by id  
@api_view(['GET'])
def batch_view(request, batch_id):
    batch = Batch.objects.get(id=batch_id)
    if request.method == 'GET':
        serializer = BatchSerializer(batch)
        return Response(serializer.data, status.HTTP_200_OK)
    
# Student view by id  
@api_view(['GET'])
def student_view(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status.HTTP_200_OK)
    
# Delete batch
@api_view(['GET','DELETE'])
def batch_delete(request, batch_id):
    batch = Batch.objects.get(id=batch_id)

    if request.method == 'GET':
        serializer = BatchSerializer(batch)
        return Response(serializer.data, status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        batch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Delete student
@api_view(['GET','DELETE'])
def student_delete(request, student_id):
    student = Student.objects.get(id=student_id)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Patch batch
@api_view(['GET','PATCH'])
def batch_edit(request, batch_id):
    try:
        batch = Batch.objects.get(id=batch_id)
    except Batch.DoesNotExist:
        return Response({'error':'Category not found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BatchSerializer(batch)
        return Response(serializer.data, status.HTTP_200_OK)
        
    elif request.method == 'PATCH':
        serializer = BatchSerializer(batch, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Patch student
@api_view(['GET','PATCH'])
def student_edit(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response({'error':'Product not found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status.HTTP_200_OK)
        
    elif request.method == 'PATCH':
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Put batch
@api_view(['GET','PUT'])
def batch_update(request, batch_id):
    try:
        batch = Batch.objects.get(id=batch_id)
    except Batch.DoesNotExist:
        return Response({'error':'Category not found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BatchSerializer(batch)
        return Response(serializer.data, status.HTTP_200_OK)
        
    elif request.method == 'PUT':
        serializer = BatchSerializer(batch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

# Put student  
@api_view(['GET','PUT'])
def student_update(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response({'error':'Product not found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status.HTTP_200_OK)
        
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)