# Generated by Django 2.2.6 on 2019-12-20 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curier', '0004_auto_20191219_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='curier',
            name='balance',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1000),
        ),
    ]
