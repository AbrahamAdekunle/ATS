# Generated by Django 4.0.6 on 2022-08-03 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
