# Generated by Django 4.0.3 on 2022-04-08 21:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portal", "0013_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="post_url",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
