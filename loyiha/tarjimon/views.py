from django.shortcuts import render
from .models import Lugat
from django.http import HttpResponse
def index(request):
    soz = request.GET.get('q','')
    if soz and soz!='':
        natija = Lugat.objects.filter(inglizcha__contains=soz).all()
    else:
        natija = None
    return render(request,'index.html',{'q':soz,'natija':natija})