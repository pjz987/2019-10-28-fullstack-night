# Generated by Django 2.2.9 on 2020-02-14 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_dos', '0003_auto_20200207_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='chore_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
    ]
