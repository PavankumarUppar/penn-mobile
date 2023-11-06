# Generated by Django 3.1.4 on 2021-01-29 20:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("gsr_booking", "0001_squashed_0011_merge_20200418_2009"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="gsrbookingcredentials",
            name="email",
        ),
        migrations.RemoveField(
            model_name="gsrbookingcredentials",
            name="id",
        ),
        migrations.AlterField(
            model_name="gsrbookingcredentials",
            name="date_updated",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="gsrbookingcredentials",
            name="session_id",
            field=models.CharField(max_length=50, null=True, verbose_name="Session ID"),
        ),
        migrations.AlterField(
            model_name="gsrbookingcredentials",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
