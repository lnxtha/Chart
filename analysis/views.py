from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Listings

from django.db.models import Count

import csv
import os
import re

# Create your views here.
class DashboardHome(View):
    def get(self, request):
        template_name = 'index.html'
        context = {
        'dash_act': 'active',
        'growthtrend': Listings.objects.raw('select  1 as id, Datepart(year,r.date) as year, l.room_type as room_type, COUNT(distinct r.id) as counter from  analysis_listings l inner join analysis_reviews r ON r.id = l.id group by Datepart(year,r.date), l.room_type'),
        'scatterboxplot': Listings.objects.raw('select distinct 1 as id,  availabilitiy_365 as availability, sum(cast(price as float)) as totalprice from analysis_listings group by availabilitiy_365 having sum(cast(price as float)) < 50000;'),
            'barchart_ascending':
         Listings.objects.raw('select top 10  1 as id, neighbourhood, count(l.id) as total from analysis_listings l join analysis_reviews r on l.id = r.id group by neighbourhood order by count(l.id) asc'),
            'barchart_descending':
         Listings.objects.raw('select top 10  1 as id, neighbourhood, count(l.id) as total from analysis_listings l join analysis_reviews r on l.id = r.id group by neighbourhood order by count(l.id) desc'),
        'piechart': Listings.objects.raw('select 1 as id, l.room_type roomtype, (Count(c.id)* 100 / (Select Count(*) From analysis_calendars)) as percentg from analysis_listings l join analysis_calendars c on l.id =  c.id group by room_type'),
            #'listofobjects':Listings.objects.raw('select distinct 1 as id, neighbourhood, round(cast(latitude as float),3), round(cast(longitude as float),3) from analysis_listings'
            'listofobjects': Listings.objects.all()[:1000]
                        }
        return render(request, template_name, context)





class PricingStrategy(View):
    def get(self,request):

        template_name = 'pricing_strategy.html'
        context = {
            'averagepricebyroomtype':Listings.objects.raw('select 1 as id,room_type, round(avg(cast(price as float)),2) as average_price from analysis_listings group by room_type order by room_type'),
            'averagepricebyroomtypeyearwise': Listings.objects.raw('select 1 as id, datepart(year,r.date) as year,l.room_type, round(avg(cast(l.price as float)),2) as average from analysis_listings l inner join analysis_reviews r on l.id=r.id group by datepart(year,r.date),l.room_type order by l.room_type'),
            'scatterplot': Listings.objects.raw('select 1 as id, price, count(l.id) as listidcount from analysis_listings l join analysis_reviews r on l.id = r.id  where price < 1500 group by price'),
            'linechart': Listings.objects.raw("select 1 as id, Datepart(year,date) as year , Datepart(month,date) as month , avg(cast(price as float)) as avg_price from analysis_listings l join analysis_reviews r on l.id = r.id where Datepart(year,date) in ('2018','2019') group by Datepart(year,date), Datepart(month,date) order by Datepart(year,date), Datepart(month,date) asc")
        }
        return render(request, template_name, context)


class CustomerSatisfaction(View):
    def get(self,request):
        template_name = 'customer_satisfaction.html'
        return render(request, template_name,{'listofobjects':
                                              Listings.objects.all()[:1000]})


class BarChart(View):
    def get(self,request):
        template_name = 'barchart.html'
        variable_to_template = 'hello'
        return render(request, template_name, {
            'barchart_ascending':
                Listings.objects.raw(
                    'select top 10  1 as id, neighbourhood, count(l.id) as total from analysis_listings l join analysis_reviews r on l.id = r.id group by neighbourhood order by count(l.id) asc'),
            'barchart_descending':
         Listings.objects.raw('select top 10  1 as id, neighbourhood, count(l.id) as total from analysis_listings l join analysis_reviews r on l.id = r.id group by neighbourhood order by count(l.id) desc'), 'bar_chart':'active'} )


class LineChart(View):
    def get(self,request):
        template_name = 'linechart.html'
        variable_to_template = 'hello'
        return render(request, template_name, {'context':variable_to_template, 'line_chart':'active'} )


class PieChart(View):
    def get(self,request):
        template_name = 'piechart.html'
        variable_to_template = 'hello'
        return render(request, template_name, {'context':variable_to_template, 'pie_chart':'active'})


class DataTable(View):
    def get(self,request):
        template_name = 'datatable.html'
        return render(request, template_name, {'datatable':'active'} )



def DataTable_Json(request, *args, **kwargs):
    data = Listings.objects.values('id','longitude', 'latitude','room_type','neighbourhood')
    return JsonResponse(data)



class Maps(View):
    def get(self, request):
        template_name = 'maps.html'
        return render(request, template_name, {'maps':'active'})



class Charts(View):
    def get(self, request):
        template_name = 'charts.html'
        return render(request, template_name, {'':''})



class Tables(View):
    def get(self, request):
        template_name = 'tables.html'
        return render(request, template_name, {'':''})


class Login(View):
    def get(self, request):
        template_name = 'login.html'
        return render(request, template_name, {'':''})


class Register(View):
    def get(self, request):
        template_name = 'register.html'
        return render(request, template_name, {'':''})


class ForgotPassword(View):
        def get(self, request):
            template_name = 'forgot-password.html'
            return render(request, template_name, {'': ''})



class AboutUs(View):
    def get(self, request):
        template_name = 'aboutus.html'
        return render(request, template_name, {'':''})




def CustomerSatisfaction_Json(request, *args, **kwargs):
    z = Listings.objects.all()
    longitude = []
    latitude = []
    room_type = []
    neighbourhood = []
    arr_string = []
    for i in z[:20]:
        longitude.append(i.longitude)
        latitude.append(i.latitude)
        room_type.append(i.room_type)
        neighbourhood.append(i.neighbourhood)

    for s in Listings.objects.all():
        arr_string.append( {
            "zoomLevel": 5,
            "scale": 0.5,
            "title": str(s.neighbourhood),
            "latitude": str(s.latitude),
            "longitude": str(s.longitude)
        })

    print(arr_string)
    return JsonResponse(
        {
            'context': arr_string
        })



