from django.shortcuts import render
import requests, json

def index(request):
    if request.method == 'POST':
        cep = request.POST.get('cep')
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

        return render(request,  'index.html', {'response': response.json()})
    else:
        return render(request,  'index.html')