from django.shortcuts import render, redirect
from .models import *
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import RetrieveAPIView ,ListAPIView ,CreateAPIView
from rest_framework import generics
class HeaderViewSet(viewsets.ModelViewSet):
    queryset = Header.objects.all()
    def get_serializer_class(self):
        if 'ar' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
            return HeaderArSerializer

        return HeaderEnSerializer
    

class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()

    def get_serializer_class(self):
        if 'ar' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
            return AboutArSerializer

        return AboutEnSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()

    def get_serializer_class(self):
        if 'ar' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
            return TagArSerializer

        return TagEnSerializer

class mision_visionViewSet(viewsets.ModelViewSet):
    queryset = mision_vision.objects.all()

    def get_serializer_class(self):
        if 'ar' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
            return mision_visionArSerializer

        return mision_visionEnSerializer
class why_homeViewSet(viewsets.ModelViewSet):
    queryset = why_home.objects.all()

    def get_serializer_class(self):
        if 'ar' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
            return why_homeArSerializer

        return why_homeEnSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()

    def get_serializer_class(self):
        if 'ar' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
            return ServiceArSerializer

        return ServiceEnSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()

    def get_serializer_class(self):
        if 'ar' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
            return ClientArSerializer

        return ClientEnSerializer




class  SubCategoryViewSet(viewsets.ModelViewSet):
    queryset =  SubCategory.objects.all()

    def get_serializer_class(self):
        if 'ar' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
            return  SubCategoryArSerializer

        return  SubCategoryEnSerializer


class ProductTuyaViewSet(viewsets.ModelViewSet):
    queryset = ProductTuya.objects.all()
  

    def get_serializer_class(self):
        if 'ar' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
            return ProductTuyaArSerializer

        return ProductTuyaEnSerializer
    def retrieve(self, request,  pk:int):
        queryset = ProductTuya.objects.get(id=pk)
        serializer = ProductTuyaSerializer( queryset,many=False)
        return Response(serializer.data)

class ProductHdlViewSet(viewsets.ModelViewSet):
    queryset = ProductHdl.objects.all()
   
    def get_serializer_class(self):
        if 'ar' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
            return ProductHdlArSerializer

        return ProductHdlEnSerializer

    def retrieve(self, request,  pk:int):
        queryset = ProductHdl.objects.get(id=pk)
        serializer = ProductHdlSerializer( queryset,many=False)
        return Response(serializer.data)

class projectViewSet(viewsets.ModelViewSet):
  
    serializer_class = ProjectSerializer
    queryset = project.objects.all()

class ContactCreateView(APIView):

    def post(self, request, format=None):
        data = self.request.data

        try:
            send_mail(
                data['subject'],
                'Name: '
                + data['name']
                + '\nEmail: '
                + data['email']
                +'\nPhone:'
                +data['phone']
               
                + '\n\nMessage:\n'
                + data['message'],
                'hautomation21@gmail.com',
                ['hautomation21@gmail.com'],
                fail_silently=False
            )

            contact = Contact(name=data['name'], email=data['email'], phone = data['phone'],subject=data['subject'], message=data['message'])
            contact.save()

            return Response({'success': 'Message sent successfully'})

        except:
            return Response({'error': 'Message failed to send'})






class VideoViewSet(viewsets.ModelViewSet):
  
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
