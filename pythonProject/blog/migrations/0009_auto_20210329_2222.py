# Generated by Django 3.1.7 on 2021-03-29 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_dt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='CREATE DATE'),
        ),
    ]
