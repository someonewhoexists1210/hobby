from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
        labels = {'text': 'Question'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-question'})

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']
        labels = {'text': 'Answer'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-answer'})

class CreationForm(forms.Form):
    question = forms.CharField(label='Question', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    answer1 = forms.CharField(label='Answer 1', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    answer2 = forms.CharField(label='Answer 2', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    answer3 = forms.CharField(label='Answer 3', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    answer4 = forms.CharField(label='Answer 4', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
