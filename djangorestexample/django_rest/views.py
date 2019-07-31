from django.shortcuts import render
from .models import Plan



# Create your views here.
def home(request):
    p=Plan.objects.all()
    print(p)
    return render(request, 'index.html',{"plan": p})