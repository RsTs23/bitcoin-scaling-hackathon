# Generated by Django 3.2.5 on 2023-04-15 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('referral_payout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='referralpayout',
            name='referring_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referring', to=settings.AUTH_USER_MODEL),
        ),
    ]
