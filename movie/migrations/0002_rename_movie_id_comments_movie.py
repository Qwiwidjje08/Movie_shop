# Generated by Django 4.2 on 2024-09-07 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='movie_id',
            new_name='movie',
        ),
    ]
