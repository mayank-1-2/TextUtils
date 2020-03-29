from django.http import HttpResponse
from django.shortcuts import render

def removepunc(djtext):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyze=""
    for i in djtext:
        if i not in punctuations:
            analyze +=i
    return analyze

def full(djtext):
        analyze=""
        for i in djtext:
            analyze+=i.upper()
        return analyze

def new(djtext):
        analyze=""
        for i in djtext:
            if i !="\n" and i!="\r":
                analyze+=i
        return analyze

def index(request):
    return render(request, 'index.html' )

def analyze(request):
    n=[]
    djtext= request.POST.get('text','default')
    removepac=request.POST.get("removepac","off")
    fullcaps=request.POST.get("fulcapitalize","off")
    newline=request.POST.get("newlineremover","off")
    t=djtext
    if removepac=="on":
        n.append(1)
    if fullcaps=="on":
        n.append(2)
    if newline=="on":
        n.append(3)
    for j in n:
        if j==1:
            t=removepunc(t)
        elif j==2:
             t=full(t)
        elif j==3:
             t=new(t)
    param={'porpouse': 'Removed Pancutation' , 'analyzed_text': t}
    return render(request,'analyze.html' , param)