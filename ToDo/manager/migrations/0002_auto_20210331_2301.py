# Generated by Django 3.1.7 on 2021-03-31 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_created',
            field=models.CharField(max_length=50),
        ),
    ]
