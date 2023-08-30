from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def home(request):
    #return HttpResponse("Olá mundo", content_type="text/plain")
    return render(request, 'MeuApp/home.html')
def about(request):
    # processamento antes de mostrar a segunda página
    return render(request, 'MeuApp/about.html')