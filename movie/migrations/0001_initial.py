# Generated by Django 4.2 on 2024-08-31 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, unique=True, verbose_name='Название категории:')),
                ('category_slug', models.SlugField(max_length=255, unique=True, verbose_name='Слаг категорий')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категорий',
            },
        ),
        migrations.CreateModel(
            name='Janr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('janr_name', models.CharField(max_length=250, verbose_name='Жанр:')),
                ('janr_slug', models.SlugField(max_length=250, verbose_name='Слаг жанра:')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=255, verbose_name='Название:')),
                ('published_date', models.DateField(verbose_name='Дата выпуска:')),
                ('image', models.ImageField(upload_to='media/posters', verbose_name='Постер:')),
                ('description', models.TextField(verbose_name='описание:')),
                ('actors', models.TextField(verbose_name='В фильме участвовали:')),
                ('country', models.TextField(max_length=255, verbose_name='Страна производства:')),
                ('video', models.FileField(upload_to='media/movies', verbose_name='Фильм')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.category')),
                ('janr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.janr')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий:')),
                ('published_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления:')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movies')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
