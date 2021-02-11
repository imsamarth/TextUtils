from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check Checkbox Values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # Check which checkbox is on
    if (removepunc == "on"):

        # analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>.?@#$%^&*'''

        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New line remover', 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Extra Space remover', 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyze.html', params)

    if (charcount == "on"):
        analyzed = len(djtext)

        params = {'purpose': 'Char Count', 'analyzed_text': analyzed}

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on":
        return HttpResponse("Please Select any Operation and try again !")

    return render(request, 'analyze.html', params)
