# Generated by Django 2.2.6 on 2020-03-13 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lallog', '0023_auto_20200313_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testorder',
            name='to_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
