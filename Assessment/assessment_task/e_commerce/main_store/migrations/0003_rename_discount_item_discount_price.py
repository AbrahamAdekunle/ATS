# Generated by Django 4.1 on 2022-08-24 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_store', '0002_alter_item_vendor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='discount',
            new_name='discount_price',
        ),
    ]
