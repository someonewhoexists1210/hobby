from django.contrib import admin
from .models import Question, Answer, Responses

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Responses)
