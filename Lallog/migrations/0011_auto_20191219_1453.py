# Generated by Django 2.2.6 on 2019-12-19 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lallog', '0010_testorder_curier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testorder',
            name='curier',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choiced_curier', to='curier.Curier'),
        ),
    ]
