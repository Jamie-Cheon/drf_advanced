# Generated by Django 3.0.7 on 2020-06-14 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_auto_20200614_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='context',
            field=models.TextField(blank=True),
        ),
    ]
