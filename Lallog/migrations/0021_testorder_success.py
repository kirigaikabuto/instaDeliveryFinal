# Generated by Django 2.2.6 on 2020-03-12 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lallog', '0020_auto_20200130_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='testorder',
            name='success',
            field=models.BooleanField(default=True),
        ),
    ]
