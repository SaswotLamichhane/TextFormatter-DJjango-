from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    return render(request, 'index.html')


def cap(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    capitalize = request.GET.get('capitalize', 'off')
    newline = request.GET.get('newlineremove', 'off')
    purpose = ''
    analyzed = ''
    if removepunc == 'on':
        puctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        for char in djtext:
            if char not in puctuations:
                analyzed = analyzed + char

        djtext = analyzed
        purpose = purpose + 'Removed Punctuation,'

    if capitalize == 'on':
        analyzed = djtext.upper()

        purpose = purpose + 'Text Capitalized,'
        djtext = analyzed
    if newline == 'on':
        analyzed = ''
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        purpose = purpose + 'New Lined Removed\n'
    elif (removepunc != "on") and (capitalize != "on") and (newline != "on"):
        return HttpResponse('<h1>Sorry!</h1> <p>please tick a checkbox</p>')

    params = {'purpose': purpose,
              'analyzed_text': analyzed,
              'djtext': djtext}

    return render(request, 'analyze.html', params)
