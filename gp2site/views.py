from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("halo")
    return render(request,'index.html')


def analyze(request):
    djtext = request.POST.get('text','default')
    rpunc = request.POST.get('removepunc','off')
    upperText = request.POST.get('upper','off')
    new_line_remover = request.POST.get('new_line_remover','off')
    space_remover = request.POST.get('space_remover','off')
    counter = request.POST.get('counter','off')
    analyzed = ""
    if rpunc == "on" or upperText =="on" or new_line_remover =="on" or space_remover =="on" or counter =="on":     
        if rpunc == "on":
            analyzed = ""
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed +char
            djtext = analyzed
            params ={ 'purpose':'Remove Punc', 'analyzed_text': analyzed}
        if upperText =="on":
            analyzed = ""
            for char in djtext:
                analyzed =  analyzed + char.upper()
            djtext = analyzed
            params ={ 'purpose':'Convert to UpperCase', 'analyzed_text': analyzed}
        if new_line_remover =="on":
            analyzed = ""
            for char in djtext:
                analyzed =  analyzed + char
            djtext = analyzed
            params ={ 'purpose':'New Line Remover', 'analyzed_text_rmove': analyzed}

        if space_remover =="on":
            analyzed = ""
            i=0
            while i< len(djtext):
                if not(djtext[i]==" " and djtext[i+1]==" "):
                    analyzed =  analyzed + djtext[i]
                i +=1
            djtext = analyzed
            params ={ 'purpose':'space Remover', 'analyzed_text': analyzed}

        if counter =="on":
            countNumber = " char count:-"+ str(len(djtext))
            analyzed = djtext 
            params ={ 'purpose':'space Remover', 'analyzed_text': analyzed,'analyzed_text_rmove': countNumber}
        return render(request, 'analyzeing.html',params)

    else:
        return HttpResponse("Plz chake box for confarmation")