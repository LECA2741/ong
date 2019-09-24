from django.shortcuts import render

'''def está criando uma função, chamada index; request é requisição; return significa retornar a pg, render renderizada, neste caso a pg index.html
'''

def index(request):
    return render(request, 'index.html'),
def sobre(request):
    return render(request, 'sobre.html'),