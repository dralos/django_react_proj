from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Student
from .serializers import *

# sms imports 
import clx.xms
import requests

@api_view(['GET', 'POST'])
def students_list(request):
    if request.method == 'GET':
        data = Student.objects.all()
        serializer = StudentSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            phone = request.data['phone']
            sendSMS(phone)
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def students_detail(request, pk):
    try:
        print('hello world iam delete update')
        print(pk)
        student = Student.objects.get(pk=pk)
        print(student)
    except Student.DoesNotExist:
        print('no student with pk:', pk, )
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# function for sending SMS 
def sendSMS(phone): 
  client = clx.xms.Client(service_plan_id='7a2d03d8440941509431fc585d4ae1c7', token='81ed088782654d5d9abce8c4a3878371')

  create = clx.xms.api.MtBatchTextSmsCreate()
  create.sender = '447537432321'
  create.recipients = {phone}
  create.body = 'This is a test message from your Sinch account'

  try:
    batch = client.create_batch(create)
  except (requests.exceptions.RequestException,
    clx.xms.exceptions.ApiException) as ex:
    print('Failed to communicate with XMS: %s' % str(ex))