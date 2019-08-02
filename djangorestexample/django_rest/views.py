from django.shortcuts import render
from .models import Plan
from .django_rest import JSONResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
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


# Create your views here.
def home(request):
    p=Plan.objects.all()
    print(p)
    return render(request, 'index.html',{"plan": p})

       
@csrf_exempt
def plan_list(request):
    if request.method == 'GET':
        #get all plans fork db
        plans = Plan.objects.all()
        plans_serializer= Planserializer(plans, many=True)                     
        #return ()
        return JSONResponse(plans_serializer.data)
    elif request.method == 'POST':
        plans_data = JSONParser().parse(request)
        plans_serializer = Planserializer(data=plans_data)
        if plans_serializer.is_valid():
            plans_serializer.save()
            return JSONResponse(plans_serializer.data,status=status.HTTP_201_CREATED)
        return JSONResponse(plans_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def plan_detail(request,pk):
    try: 
        plan = Plan.objects.get(pk=pk)
    except Plan.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        plans_serializer = Planserializer(plan)
        return JSONResponse(plans_serializer.data)
    elif request.method == "PUT":
        plan_data = JSONParser().parse(request)
        plans_serializer = Planserializer(plan, data = plan_data)
        if plans_serializer.is_valid():
            plans_serializer.save()
            return JSONResponse(plans_serializer.data)
        return JSONResponse(plans_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        plan.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)