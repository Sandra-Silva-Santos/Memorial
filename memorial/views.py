from django.shortcuts import render
from .models import Memorial
from django.db.models import Q





def index(request):
    return render(request, 'index.html')


def obtuario(request):
    results = []
    falecido = request.GET.get('search')
    if falecido:
        results = Memorial.objects.filter(Q(falecido__icontains=falecido))
    return render(request, 'obtuario.html', {'results': results})






    




    