from django.http import HttpResponse
from django.shortcuts import render


def details(request):
    return render(request,'details_data.html')
    #return HttpResponse("Hello, world. You're at the polls index.")