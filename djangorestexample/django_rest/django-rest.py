from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_token
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Plan
from .serializers import Planserializer

class JSONResponse(HttpResponse):
    def __init__(self,data,**kwargs):
        #converting python primitive to JSON data
        content = JSONRenderer().render(data)
        #adding conetent_type key to response header
        kwargs['content_type']='application/json'
        super(JSONResponse, self).__init__(content, **kwargs)