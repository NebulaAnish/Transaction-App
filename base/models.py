from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(
        default='default.png', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username


class Transaction(models.Model):
    category_choices = (('Income', "Income"), ("Expense", "Expense"))
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    category = models.CharField(max_length=7, choices=category_choices)

    def __str__(self):
        return self.title
