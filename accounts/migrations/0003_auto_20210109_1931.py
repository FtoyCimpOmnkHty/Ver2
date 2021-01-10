# Generated by Django 3.1.4 on 2021-01-09 10:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_roomcheck'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeestate',
            name='regist_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='roomcheck',
            name='regist_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
