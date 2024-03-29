# Generated by Django 4.0.6 on 2022-08-02 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_article_tags_alter_comment_article_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date_uploaded']},
        ),
        migrations.AddField(
            model_name='author',
            name='author_picture',
            field=models.ImageField(blank=True, null=True, upload_to='author_images'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='article_images/'),
        ),
    ]
