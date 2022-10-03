
from django.shortcuts import render

from home.model import graph

# Create your views here.

def home(request):
    return render(request,'D:\Mini_Project\GoogleSearchAnalysis\templates\home.html')

def result(request):
    searchQueury =request.GET['search']
    uri = graph(searchQueury)
    return render(request,'result.html',{'result':searchQueury ,'data':uri})