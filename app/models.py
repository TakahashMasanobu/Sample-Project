from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Book(models.Model):
    """本"""
    title = models.CharField('タイトル', max_length=200)
    price = models.IntegerField(default=1000)
    description = models.TextField('説明')
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.title


class BuyingHistory(models.Model):
    """購入履歴"""
    book = models.ForeignKey(Book, verbose_name='購入書籍', on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='購入ユーザー', on_delete=models.PROTECT)
    is_sended = models.BooleanField('発送フラグ', default=False)
    stripe_id = models.CharField('タイトル', max_length=200)
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return '{} {} {}'.format(self.book, self.user.email, self.is_sended)
