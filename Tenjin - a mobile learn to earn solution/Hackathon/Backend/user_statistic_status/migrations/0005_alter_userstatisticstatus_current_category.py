# Generated by Django 3.2.5 on 2023-01-24 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_statistic_status', '0004_userstatisticstatus_current_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstatisticstatus',
            name='current_category',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
