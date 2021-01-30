# Generated by Django 2.2.12 on 2021-01-30 07:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='language',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]