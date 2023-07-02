from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from .models import Moto
from .serializers import MotoSerializer

# Create your views here.

class MotoListApiView(APIView):
    def get(self, request, *args, **kwargs):
        motos=Moto.objects
        serializer = MotoSerializer(motos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data={
            'trademark': request.data.get('trademark'),
            'model': request.data.get('model'),
            'reference': request.data.get('reference'),
            'price': request.data.get('price'),
            'image': request.data.get('image'),
            'supplier': request.data.get('supplier'),
        }
        serializer = MotoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


