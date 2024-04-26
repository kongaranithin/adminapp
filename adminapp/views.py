from django.shortcuts import render
from django.views import View
from .models import Product
class DisplayView(View):
    def get(self,request):
        qs=Product.objects.all()
        con_dict={"records":qs}
        return render(request, 'display.html',con_dict)# Create your views here.
