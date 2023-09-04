from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import HttpResponse 
from django.http import JsonResponse

from .models import TodoModel
from .serializers import TodoSerializer
# Create your views here.

@api_view(['GET','POST'])
def gettodolist(request):
    if request.method == 'GET':
        todo=TodoModel.objects.all()
        serializee=TodoSerializer(todo,many=True)
        return JsonResponse({'data' :serializee.data})
    if request.method =='POST':
        print(request.data)
        serialize= TodoSerializer(data=request.data)
        if serialize.is_valid():
            # Save the validated data to the database
            serialize.save()    

            print('hhhh')
            return JsonResponse({'ddd':'hh'})
        else:
            return JsonResponse(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
        
    

        # todolist=TodoModel.objects.create(task=request.POST['task'],status=request.POST['status'],Priority=request.POST['priority'])
    # return Response({'msg':'h'})

        

    
        
