from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from django.db import close_old_connections
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

# Create your views here.
from .models import istanbulNufus
from .serializers import istanbulNufusSerializer

class istanbulNufusList(generics.ListAPIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission

    serializer_class = istanbulNufusSerializer
    queryset = istanbulNufus.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['year']
    filterset_fields = ['year']
    '''
    def get(self, request, format=None):
        
        tufeList = Tufe.objects.all().order_by('-date')
        serializer = TufeSerializer(weatherList, many=True)
        response = Response(serializer.data) 
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "*"

        return response
    '''
    
    def post(self, request):
        serializer = istanbulNufusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            close_old_connections()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        close_old_connections()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        istanbulNufusList = istanbulNufus.objects.all()
        operation = istanbulNufusList.delete()
        data ={}
        if operation: 
            data['success'] = "delete successful"
        else:
            data['failed'] = "delete failed"
        return  Response(data=data)

class istanbulNufusDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = istanbulNufus.objects.all()
    serializer_class = istanbulNufusSerializer
    filter_backends = [DjangoFilterBackend]
