from django.db import models

class Question(models.Model):
    subtest = models.IntegerField(default=lambda: Question.objects.latest('subtest').subtest
                                if Question.objects.exists() else 0)
    nomor = models.IntegerField(default=lambda: Question.objects.latest('nomor').nomor + 1
                                if Question.objects.exists() else 1)
    question_text = models.TextField(default='what ?')
    choiceA = models.CharField(max_length=200, default='a')
    choiceB = models.CharField(max_length=200, default='b')
    choiceC = models.CharField(max_length=200, default='c')
    choiceD = models.CharField(max_length=200, default='d')
    choiceE = models.CharField(max_length=200, default='e')
    ans = models.CharField(max_length=50, default='a')
    def __str__(self) -> str:
        return ''.join([str(self.nomor), '  ', self.question_text])

class Person(models.Model):
    nama = models.CharField(max_length=50)
    nik = models.CharField(max_length=50)
    no_peserta = models.CharField(max_length=50)
    jurusan = models.CharField(max_length=50)
    subtest1 = models.IntegerField(default=0)
    subtest2 = models.IntegerField(default=0)
    subtest3 = models.IntegerField(default=0)
    subtest4 = models.IntegerField(default=0)
    nilai = models.IntegerField(default=0)

    def __str__(self) -> str:
        return '---'.join([self.nama, self.no_peserta])