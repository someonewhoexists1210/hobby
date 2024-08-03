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