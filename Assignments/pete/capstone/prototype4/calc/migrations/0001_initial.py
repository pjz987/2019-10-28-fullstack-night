# Generated by Django 2.2.9 on 2020-02-11 22:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Macros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meas_sys', models.BooleanField()),
                ('weight', models.IntegerField()),
                ('bfp', models.IntegerField()),
                ('act_lvl', models.FloatField()),
                ('goal', models.BooleanField()),
                ('lbm', models.IntegerField()),
                ('bmr', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('train_kcal', models.IntegerField()),
                ('train_fat', models.IntegerField()),
                ('train_carb', models.IntegerField()),
                ('rest_kcal', models.IntegerField()),
                ('rest_fat', models.IntegerField()),
                ('rest_carb', models.IntegerField()),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='macros', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
