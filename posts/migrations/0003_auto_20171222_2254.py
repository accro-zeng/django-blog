# Generated by Django 2.0 on 2017-12-22 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20171222_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='modified_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]