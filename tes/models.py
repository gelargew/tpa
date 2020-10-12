from django.db import models
from django import forms

class Question(models.Model):
    nomor = models.IntegerField(default=0)
    question_text = models.CharField(max_length=999)
    choice1 = models.CharField(max_length=200)
    choice2 = models.CharField(max_length=200)
    choice3 = models.CharField(max_length=200)
    choice4 = models.CharField(max_length=200)
    ans = models.CharField(max_length=200)
    def __str__(self) -> str:
        return ''.join([str(self.nomor), '  ', self.question_text])

class Person(forms.Form):
    name = forms.CharField(max_length=50)
    date_of_birth = forms.DateField()
    birthplace = forms.CharField(max_length=50)
    education = forms.CharField(max_length=50, required=False)
    address = forms.CharField(max_length=200)
    test_id = forms.CharField(max_length=20)
    #result = forms.IntegerField(default=0)

