# Generated by Django 4.2.4 on 2023-10-19 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webflut', '0012_breakfast_products_date_dinner_products_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='breakfast_products',
            name='weight',
            field=models.TextField(default=0),
        ),
    ]
