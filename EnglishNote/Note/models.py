from unicodedata import category
from django.db import models
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    # 問題カテゴリ
    name = models.CharField('カテゴリ名', max_length=255)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        # テキストの値を返す
        return self.name


class Post(models.Model):
    # 問題本文と答え
    question = models.TextField('問題文')
    answer = models.TextField('答え')
    created_at = models.DateTimeField('作成日', default=timezone.now)
    # on_delete=models.PROTECT だと子のデータを消さないと親のデータは消せない
    category = models.ForeignKey(
        Category, verbose_name='カテゴリ', on_delete=models.PROTECT)

    def __str__(self):
        # テキストの値を返す
        return self.question
