# Generated by Django 4.1 on 2022-08-18 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.ImageField(default="avatar.svg", null=True, upload_to=""),
        ),
    ]
