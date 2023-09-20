# Generated by Django 3.2.5 on 2023-09-19 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20230919_0716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='phone',
        ),
        migrations.AddField(
            model_name='settings',
            name='email',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='郵件'),
        ),
    ]
