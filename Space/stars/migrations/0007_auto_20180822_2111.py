# Generated by Django 2.0.1 on 2018-08-22 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stars', '0006_auto_20180822_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='picture',
            field=models.ImageField(upload_to='space_upload'),
        ),
    ]
