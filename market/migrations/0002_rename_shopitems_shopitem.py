# Generated by Django 4.1.3 on 2022-11-21 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShopItems',
            new_name='ShopItem',
        ),
    ]