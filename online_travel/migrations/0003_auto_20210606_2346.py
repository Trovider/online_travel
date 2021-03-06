# Generated by Django 3.1.3 on 2021-06-06 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('online_travel', '0002_spot_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='m',
        ),
        migrations.AddField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
