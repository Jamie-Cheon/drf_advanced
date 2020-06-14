from django.contrib.auth.models import User
from django.db import models


class Card(models.Model):
    class NameChoice(models.TextChoices):
        DEBIT = 'debit'
        CREDIT = 'credit'

    name = models.CharField(choices=NameChoice.choices, max_length=30)
    context = models.TextField(blank=True)
    is_reported = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='created')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cards')

    def __str__(self):
        return self.name

