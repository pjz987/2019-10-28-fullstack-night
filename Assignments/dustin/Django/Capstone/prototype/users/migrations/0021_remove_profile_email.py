# Generated by Django 3.0.3 on 2020-03-08 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20200308_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
