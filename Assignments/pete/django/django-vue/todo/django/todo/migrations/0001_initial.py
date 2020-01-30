# Generated by Django 2.2.9 on 2020-01-30 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=140)),
                ('created', models.DateTimeField(auto_now=True)),
                ('completed', models.DateTimeField(null=True)),
                ('completed_bool', models.BooleanField(default=False)),
            ],
        ),
    ]
