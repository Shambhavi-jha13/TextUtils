# I have created this file - Shambhavi
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    capalpha = request.POST.get('capalpha','off')
    newlineremove = request.POST.get('newlineremove','off')
    removespace = request.POST.get('removespace','off')
    charcount= request.POST.get('charcount','off')

    if removepunc == "on":
        punctuations = ''',./";:=+-*!@#$^&%()_[]'<>{}'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'removed punctuations','analyzed_text': analyzed}
        djtext = analyzed

    if(capalpha=="on"):
        analyzed= ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremove=="on"):
        analyzed= ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'remove the new line', 'analyzed_text': analyzed}
        djtext = analyzed

    if(removespace=="on"):
        analyzed= ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1])== " ":
                analyzed = analyzed + char
        params = {'purpose': 'remove the extra space', 'analyzed_text': analyzed}
        djtext = analyzed
        return render(request, 'analyze.html', params)
    if(charcount=="on"):
        analyzed=0
        for index,char in enumerate(djtext):
            if djtext[index] != " ":
                analyzed=analyzed+1
        params = {'purpose': 'count the number of characters', 'analyzed_text': analyzed}
        djtext = analyzed
        return render(request, 'analyze.html', params)
    if(removepunc!= "on" and capalpha!="on" and newlineremove!="on" and removespace!="on" and charcount!="on"):
        return HttpResponse("Please select the operations and try again!!")
    return render(request, 'analyze.html', params)

