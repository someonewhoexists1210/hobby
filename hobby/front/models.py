from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=255)  # The question text

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self, question=False):
        if question:
            return f"{self.text} (Question: {self.question.text})"
        else:
            return self.text

class Responses(models.Model):
    question = models.ForeignKey(Question, related_name='responses', on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, related_name='responses', on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()

    def __str__(self):
        return f"Question: {self.question.text}"