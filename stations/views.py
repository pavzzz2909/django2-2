from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


from pprint import pprint

def index(request):
    return redirect(reverse('bus_stations'))


with open('data-398-2018-08-30.csv',encoding='utf-8',newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    CONTENT = [dict(i) for i in reader]


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    page_num = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_num)
    context = {
        'page': page,
    }
    return render(request, 'stations/index.html', context)
