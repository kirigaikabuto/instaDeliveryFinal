# Generated by Django 2.2.6 on 2020-03-13 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lallog', '0026_auto_20200313_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testorder',
            name='to_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
