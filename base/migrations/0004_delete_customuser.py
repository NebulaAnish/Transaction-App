# Generated by Django 4.2.1 on 2023-06-04 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]