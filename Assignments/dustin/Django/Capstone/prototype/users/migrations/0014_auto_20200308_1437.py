# Generated by Django 3.0.3 on 2020-03-08 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20200308_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layout',
            name='text',
            field=models.CharField(default=1, max_length=150),
        ),
        migrations.AlterField(
            model_name='theme',
            name='text',
            field=models.CharField(default=1, max_length=150),
        ),
    ]