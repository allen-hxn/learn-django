from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext, loader
from .models import Person
# Create your views here.

def index(request):
    person_list = Person.objects.order_by('id')[:5]
    context = {'person_list': person_list}
    return render(request, 'index.html', context)

def detail(request):
    try:
        person_id = request.GET['id']
        person = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        raise Http404("Person does not exist")
    return render(request, 'details.html', {"person": person})
