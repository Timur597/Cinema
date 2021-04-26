from django.db import models
from django.urls import reverse


class MovieShots(models.Model):
    title = models.CharField(max_length=255, verbose_name='Кадры фильма')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры фильма'


class Feedback(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255, verbose_name='Автор отзыва')
    text = models.TextField(verbose_name='Отзыв')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class StarsRating(models.Model):
    stars_rating = models.IntegerField(verbose_name='Рейтинг актёра')

    def __str__(self):
        return self.stars_rating

    class Meta:
        ordering = ['stars_rating']
        verbose_name = 'Рейтинг актёра'
        verbose_name_plural = 'Рейтинг актёров'


class Actors(models.Model):
    name = models.CharField(max_length=255, verbose_name='Актёр')
    age = models.IntegerField(verbose_name='Возраст')
    description = models.TextField(verbose_name='Биография')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    stars_rating = models.ForeignKey(StarsRating, on_delete=models.CASCADE, verbose_name='Рейтинг актёра')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Актрёр'
        verbose_name_plural = 'Актёры'


class Rating(models.Model):
    stars = models.IntegerField(verbose_name='Рейтинг фильма')

    def str(self):
        return self.stars

    class Meta:
        ordering = ['stars']
        verbose_name = 'Рейтинг фильма'
        verbose_name_plural = 'Рейтинг фильмов'


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Категория')
    slug = models.SlugField(max_length=255, verbose_name='Ссылка', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})


class Genre(models.Model):
    title = models.CharField(max_length=255, verbose_name='Жанр')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(max_length=255, verbose_name='Ссылка', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Staff(models.Model):
    name = models.CharField(max_length=255, verbose_name='Режисёр')
    age = models.IntegerField(verbose_name='Возраст')
    description = models.TextField(verbose_name='Биография')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Коллектив'
        verbose_name_plural = 'Коллектив'


class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slogan = models.CharField(max_length=255, verbose_name='Слоган')
    description = models.TextField(verbose_name='описание', blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Постер')
    year = models.DateField(verbose_name='Год выпуска', blank=True)
    country = models.CharField(max_length=255, verbose_name='Страна создания')
    staff = models.ManyToManyField(Staff, verbose_name='Коллектив')
    actors = models.ManyToManyField(Actors, verbose_name='Актеры')
    genre = models.ManyToManyField(Genre, verbose_name='Жанры', blank=True)
    world_premiere = models.CharField(max_length=255, verbose_name='Примеьра в мире')
    budget = models.CharField(max_length=255, verbose_name='Бюджет')
    fees_USA = models.CharField(max_length=255, verbose_name='Сборы в сша')
    fees_world = models.CharField(max_length=255, verbose_name='Сборы в мире')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', blank=True)
    slug = models.SlugField(max_length=255, verbose_name='Ссылка', unique=True)
    feedback = models.ManyToManyField(Feedback, verbose_name='Отзывы')
    rating = models.ManyToManyField(Rating, verbose_name='Рейтинг')
    movie_shots = models.ManyToManyField(MovieShots, verbose_name='Кадры из фильма')

    def get_absolute_url(self):
        return reverse('movie', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
