
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def count(request):
    text=request.GET["full_text"]

    words=text.split(" ")

    dictonary={}

    for k in words:
        if len(k)==0:
            continue
        if not k in dictonary.keys():
            dictonary[k]=1
        else:
            dictonary[k]+=1



    return render(request, "count.html",{'length':dictonary.items()})

def about(request):
    return render(request,"about.html")
