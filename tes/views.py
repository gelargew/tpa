from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Question, Person

def index(request):
    soal = Question.objects.order_by('nomor')
    template = loader.get_template('tes/index.html')
    context = {
        'question_list': soal,
    }
    return HttpResponse(template.render(context, request))

def login(request):
    name = 'not logged in'
    if request.method == 'POST':
        PersonForm = Person(request.POST)

        if PersonForm.is_valid():
            name = PersonForm.cleaned_data['name']
    else:
        PersonForm = Person()
    
    return render(request, 'tes/login.html', {'name': name})
