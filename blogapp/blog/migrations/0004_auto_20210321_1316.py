# Generated by Django 3.1.7 on 2021-03-21 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210321_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_dt',
            field=models.DateTimeField(verbose_name='CREATE DATE'),
        ),
        migrations.AlterField(
            model_name='post',
            name='modify_dt',
            field=models.DateTimeField(verbose_name='MODIFY DATE'),
        ),
    ]
