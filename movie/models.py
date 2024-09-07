from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=255,verbose_name='Название категории:',unique=True)
    category_slug = models.SlugField(verbose_name='Слаг категорий',max_length=255,unique=True)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'

        def __str__(self):
            return self.category_name
        
class Janr(models.Model):
    janr_name = models.CharField(max_length=250,verbose_name='Жанр:')
    janr_slug = models.SlugField(max_length=250,verbose_name='Слаг жанра:')
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

        def __str__(self):
            return self.janr_name
        
class Movies(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.TextField(max_length=255,verbose_name='Название:')
    published_date = models.DateField(verbose_name='Дата выпуска:')
    janr = models.ForeignKey(Janr,on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Постер:',upload_to='media/posters')
    description = models.TextField(verbose_name='описание:')
    actors = models.TextField(verbose_name='В фильме участвовали:')
    country = models.TextField(verbose_name='Страна производства:',max_length=255)
    video = models.FileField(upload_to='media/movies',verbose_name='Фильм')


class Comments(models.Model):
    text = models.TextField(verbose_name='Комментарий:')
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies,on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True,verbose_name='Дата добавления:')
    

