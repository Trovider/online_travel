# Generated by Django 3.1.3 on 2021-06-12 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_travel', '0005_auto_20210612_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spot',
            name='explanation',
        ),
        migrations.AddField(
            model_name='spot',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='description'),
        ),
    ]
