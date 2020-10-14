from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from .models import Question, Person


#subtest1
def index(request):
    soal = Question.objects.filter(subtest='1').order_by('nomor')
    if not soal:
        return render(request, 'tes/finish.html')
    template = loader.get_template('tes/index.html')
    context = {
        'question_list': soal,
    }
    answer = request.POST
    if request.POST.get('selesai') == 'selesai':
        nilai = 0
        print('submitted')
        for num in range(1, len(soal)):
            answer = request.POST.get(str(num))
            kunci = Question.objects.filter(nomor=num, subtest='1')
            if len(kunci) == 1:
                kunci = Question.objects.get(nomor=num, subtest='1').ans
                if kunci.lower() == answer:
                    nilai += 1
        current_user = request.POST.get('no_peserta')
        if current_user:
            peserta = Person.objects.filter(no_peserta=current_user)
            for people in peserta:
                people.subtest1 = nilai
                people.nilai = nilai
                people.save()
        return HttpResponseRedirect(reverse('subtest2'))
    return HttpResponse(template.render(context, request))

#subtest2
def subtest2(request):
    soal = Question.objects.filter(subtest='2').order_by('nomor')
    if not soal:
        return render(request, 'tes/finish.html')
    template = loader.get_template('tes/subtest2.html')
    context = {
        'question_list': soal,
    }
    answer = request.POST
    
    if request.POST.get('selesai') == 'selesai':
        nilai = 0
        print('submitted')
        for num in range(1, len(soal)):
            n = num + 10
            answer = request.POST.get(str(n))
            kunci = Question.objects.filter(nomor=n, subtest='2')
            if len(kunci) == 1:
                kunci = Question.objects.get(nomor=n, subtest='2').ans
                if kunci.lower() == answer:
                    nilai += 1
        current_user = request.POST.get('no_peserta')
        if current_user:
            x = Person.objects.get(no_peserta=current_user)
            x.subtest2 = nilai
            x.nilai = x.subtest1 + x.subtest2 + x.subtest3 + x.subtest4
            x.save()
            return HttpResponseRedirect(reverse('subtest3'))
    return HttpResponse(template.render(context, request))

#subtest3
def subtest3(request):
    soal = Question.objects.filter(subtest='3').order_by('nomor')
    if not soal:
        return render(request, 'tes/finish.html')
    template = loader.get_template('tes/subtest3.html')
    context = {
        'question_list': soal,
    }
    answer = request.POST
    
    if request.POST.get('selesai') == 'selesai':
        nilai = 0
        print('submitted')
        for num in range(1, len(soal)):
            n = num + 20
            answer = request.POST.get(str(n))
            kunci = Question.objects.filter(nomor=n, subtest='3')
            if len(kunci) == 1:
                kunci = Question.objects.get(nomor=n, subtest=3).ans
                if kunci.lower() == answer:
                    nilai += 1
        print('nilai: ', nilai)
        current_user = request.POST.get('no_peserta')
        if current_user:
            x = Person.objects.get(no_peserta=current_user)
            x.subtest3 = nilai
            x.nilai = x.subtest1 + x.subtest2 + x.subtest3 + x.subtest4
            x.save()
            return HttpResponseRedirect(reverse('subtest4'))
    return HttpResponse(template.render(context, request))


def subtest4(request):
    soal = Question.objects.filter(subtest='4').order_by('nomor')
    if not soal:
        return render(request, 'tes/finish.html')
    template = loader.get_template('tes/subtest4.html')
    context = {
        'question_list': soal,
    }
    answer = request.POST
    
    if request.POST.get('selesai') == 'selesai':
        nilai = 0
        print('submitted')
        for num in range(1, len(soal)):
            n = num + 30
            answer = request.POST.get(str(n))
            kunci = Question.objects.filter(nomor=n, subtest='4')
            if len(kunci) == 1:
                kunci = Question.objects.get(nomor=n, subtest='4').ans
                if kunci.lower() == answer:
                    nilai += 1
        print('nilai: ', nilai)
        current_user = request.POST.get('no_peserta')
        print(current_user)
        if current_user:
            x = Person.objects.get(no_peserta=current_user)
            x.subtest4 = nilai
            x.nilai = x.subtest1 + x.subtest2 + x.subtest3 + x.subtest4
            x.save()
            return HttpResponseRedirect(reverse('finish'))
    return HttpResponse(template.render(context, request))



def login(request):
    context = {}
    form = request.POST
    if form['no_peserta']:
        p = Person(nama=form['name'], nik=form['nik'], no_peserta=form['no_peserta'], jurusan=form['jurusan'])
        if not Person.objects.filter(no_peserta=form['no_peserta']):
            p.save()
            print('p saved')
        context.update({'no_peserta': form['no_peserta']})
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'tes/login.html')


def finish(request):
    return render(request, 'tes/finish.html')