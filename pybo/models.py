from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) ## Author User 
    modify_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f'제목 : {self.subject}'

class Answer(models.Model):
    # on_delete=models.CASCADE는 답변에 연결된 질문이 삭제되면 답변도 함께 삭제하라는 의미
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f'제목 : {self.content}'

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date=models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question=models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer=models.ForeignKey(Answer,null=True, blank=True, on_delete=models.CASCADE)