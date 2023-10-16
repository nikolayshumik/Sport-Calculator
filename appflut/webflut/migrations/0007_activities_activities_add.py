# Generated by Django 4.2.4 on 2023-10-16 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import webflut.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webflut', '0006_breakfast_products_user_snack_products_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('calories_in', models.TextField()),
                ('time', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Activities_Add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webflut.activities')),
                ('user', models.ForeignKey(default=webflut.models.get_default_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]