# Generated by Django 3.2.7 on 2021-10-04 02:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0004_auto_20210324_1851"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="degrees",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="expected_graduation",
        ),
        migrations.DeleteModel(
            name="Degree",
        ),
    ]
