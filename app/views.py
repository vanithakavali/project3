from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def third1(request):
    return HttpResponse('VIRAT KHOLI BIOGRAPHY')
def third(request):
    return render(request,'third.html')