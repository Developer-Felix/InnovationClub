# Generated by Django 3.1.3 on 2020-11-20 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20201120_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leader',
            name='slug',
            field=models.SlugField(),
        ),
    ]
