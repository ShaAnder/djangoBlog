# Generated by Django 4.2.17 on 2025-01-14 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='excript',
            field=models.TextField(blank=True),
        ),
    ]
