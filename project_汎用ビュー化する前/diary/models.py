from django.db import models
from django.utils import timezone

# Create your models here.
class Day(models.Model):
    #id = models.AutoField(primary_key=True)これは自動で作成されるから書かなくても良い
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default = timezone.now)
