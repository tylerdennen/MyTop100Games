# Generated by Django 3.0.6 on 2020-05-21 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date_released',
            field=models.DateField(blank=True),
        ),
    ]