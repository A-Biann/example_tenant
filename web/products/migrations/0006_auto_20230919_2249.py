# Generated by Django 3.2.5 on 2023-09-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20230919_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='name_en',
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='建立日期'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='modified',
            field=models.DateField(auto_now=True, verbose_name='修改日期'),
        ),
    ]
