from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Transaction(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    category_choices = (('Income', "Income"), ("Expense", "Expense"))
    category = models.CharField(max_length=7, choices=category_choices)

    def __str__(self):
        return self.title
