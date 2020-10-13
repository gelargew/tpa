from django.contrib import admin
from .models import Question, Person


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['subtest', 'nomor', 'question_text']

class PersonAdmin(admin.ModelAdmin):
    list_display = ['no_peserta', 'nik', 'nama', 'subtest1', 'subtest2', 'subtest3', 'subtest4', 'nilai']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Person, PersonAdmin)