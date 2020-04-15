from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')


def analyze(request):
    if request.method == 'POST':
        user_text = request.POST.get('user_text', 'default')
        removepunc = request.POST.get('removepunc', 'off')
        uppercase = request.POST.get('uppercase', 'off')
        newlineremover = request.POST.get('newlineremover', 'off')
        purposes = []
        analyzed_text = user_text

        if removepunc == 'on':
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            analyzed_text = ""
            for char in user_text:
                if char not in punctuations:
                    analyzed_text += char
            purposes.append('Removed Punctuations')

        if uppercase == 'on':
            analyzed_text = analyzed_text.upper()
            purposes.append('Uppercased')
        if newlineremover == 'on':
            temp = analyzed_text
            analyzed_text = ""
            for char in temp:
                analyzed_text = analyzed_text + char

        data = {
            'purposes': purposes,
            'analyzed_text': analyzed_text,
        }
        return render(request, 'index.html', data)



