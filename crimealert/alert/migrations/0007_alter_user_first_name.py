# Generated by Django 4.1.6 on 2023-02-13 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0006_auto_20230213_0423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
