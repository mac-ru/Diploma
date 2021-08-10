from django.shortcuts import render, redirect
import json
import requests
#import pprint

# Create your views here.

from myweb.models import cntr
from myweb.models import cdata
from django.contrib.auth import settings

def updatedata(request):
    if not request.user.is_authenticated:
        return render(request, 'nologin.html')

    url = "https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/2021-01-01/2021-12-31" 
    r = requests.get(url)
    data = json.loads(r.text)
    mylist = {}
    for country in data["countries"]:
        for date in data["data"]:
            if country in data["data"][date]: 
                if data["data"][date][country]["deaths"] is None:
                    data["data"][date][country]["deaths"] = 0
                if data["data"][date][country]["confirmed"] is None:
                    data["data"][date][country]["confirmed"] = 0
                new_cdata = cdata(                        
                        cd=data["data"][date][country]["country_code"]+"_"+data["data"][date][country]["date_value"],
                        code=data["data"][date][country]["country_code"],
                        date=data["data"][date][country]["date_value"],
                        confirmed=data["data"][date][country]["confirmed"],
                        deaths=data["data"][date][country]["deaths"],
                        stringency_actual=data["data"][date][country]["stringency_actual"],
                        stringency=data["data"][date][country]["stringency"]
                        )
                new_cdata.save()




   

    content = {
    'data':data["data"],
    'countries':data["countries"],
    }
    return render(request, 'updatedata.html', content)

def updatecountry(request):
#   if not request.user.is_authenticated:
#        return redirect('../')

   if not request.user.is_authenticated:
        return render(request, 'nologin.html')


   url = "https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/2021-01-01/2021-12-31"
   r = requests.get(url)
   data = json.loads(r.text)
   allc = cntr.objects.all().delete()
   for country in data["countries"]:
        new_country = cntr(
                name=country,
        )

        new_country.save()

   allc = cntr.objects.all()
   content = {
   'countries': allc
   }
   return render(request, 'updatecountry.html', content)


def showcountry(request,country="False"):

    allc = cntr.objects.all
    data = cdata.objects.order_by('deaths').filter(code=country)

    content = {
    'countries': allc,
    'data': data
    }
    return render(request, 'showcountry.html', content)


def showallcountry(request,country="False"):
    
    allc = cntr.objects.all
    data = cdata.objects.filter(code="RUS")
    content = {
    'countries': allc,
    'data': data
    }
    return render(request, 'showallcountry.html', content)

def nothing(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'menu.html')

