# Generated by Django 4.1.2 on 2023-03-13 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Product",
            new_name="Blogpost",
        ),
    ]
