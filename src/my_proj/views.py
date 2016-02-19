from django.views import generic
from accounts.models import Menu 
from django.http import HttpResponse
from django.shortcuts import render

class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"

def truptiNC(request):
    #menu = Menu.objects.values('item_name')
    #price = Menu.objects.values('price')
    menu = Menu.objects.all()
    return render(request, 'menutr.html', {'trupti':menu})

class TruptiNC(generic.TemplateView):
    template_name = "menutr.html"

   #def get_queryset(self):
		#menus = Menu.objects.all()
		#menu_items = []
		#for menu in menus:
			#if menu.nc.username =='GBNC':
                        #menu_items.append(menu.item_name)
		#print("*******************************")
		#print(menu_items[0])
		#Sreturn render(request, 'menutr.html', {'trupti':menus.item_name[0]})

class GBNC(generic.TemplateView):
    template_name = "menugb.html"

def GBNC(request):
    #menu = Menu.objects.values('item_name')
    #price = Menu.objects.values('price')
    menu = Menu.objects.all()
    return render(request, 'menugb.html', {'GBNC':menu})

class prashNC(generic.TemplateView):
    template_name = "menup.html"
