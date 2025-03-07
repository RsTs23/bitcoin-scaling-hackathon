# Generated by Django 3.2.5 on 2022-12-13 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chapter', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChapterAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collected_Sats', models.PositiveIntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('no-completed', 'no-completed'), ('completed', 'completed')], default='no-completed', max_length=20, verbose_name='status')),
                ('is_first_time', models.BooleanField(blank=True, default=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chapter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chapter.chapter')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
