# Generated by Django 3.0.3 on 2020-03-10 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20200309_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layout',
            name='text',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='theme',
            name='text',
            field=models.CharField(max_length=150),
        ),
    ]
