# Generated by Django 4.1.2 on 2023-03-13 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("post_id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(default="", max_length=50)),
                ("head0", models.CharField(default="", max_length=500)),
                ("head1", models.CharField(default="", max_length=500)),
                ("head2", models.CharField(default="", max_length=500)),
                ("pub_date", models.DateField()),
                ("thumbnail", models.ImageField(default="", upload_to="shop/images")),
            ],
        ),
    ]
