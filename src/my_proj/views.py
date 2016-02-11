from django.views import generic
from accounts.models import Menu 
from django.http import HttpResponse

class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"

class TruptiNC(generic.TemplateView):
    template_name = "menutr.html"

    def get_queryset(request):
		menus = Menu.objects.all()
		menu_items = []
		#for menu in menus:
			#if menu.nc.username =='GBNC':
                        #menu_items.append(menu.item_name)
		print("*******************************")
		print(menu_items[0])
		return render(request, 'menutr.html', {'trupti':menus.item_name[0]})

class GBNC(generic.TemplateView):
    template_name = "menugb.html"

class prashNC(generic.TemplateView):
    template_name = "menup.html"
