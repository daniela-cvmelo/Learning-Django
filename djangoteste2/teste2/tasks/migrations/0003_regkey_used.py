# Generated by Django 5.1.6 on 2025-03-23 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0002_rename_reg_key_user_reg_key_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="regkey",
            name="used",
            field=models.BooleanField(default=False),
        ),
    ]
