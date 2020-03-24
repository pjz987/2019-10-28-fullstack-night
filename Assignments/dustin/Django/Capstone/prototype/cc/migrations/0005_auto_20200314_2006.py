# Generated by Django 3.0.3 on 2020-03-15 03:06

import cc.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_auto_20200310_1951'),
        ('cc', '0004_artpiece_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='artpiece',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=cc.models.user_directory_path),
        ),
        migrations.AddField(
            model_name='artpiece',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='CollectionPiece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=cc.models.user_directory_path)),
                ('text', models.TextField(blank=True, null=True)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cc.ArtCollection')),
            ],
        ),
    ]