# Generated by Django 3.0.6 on 2020-05-21 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0003_auto_20200521_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.URLField(null=True),
        ),
    ]
