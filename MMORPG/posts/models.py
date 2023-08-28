from django.db import models
from django.contrib.auth.models import User
from django.core.cache import cache


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.authorUser.username


class Category(models.Model):

    TANKS = 'TK'
    HEALERS = 'HL'
    DAMAGEDEALER = 'DD'
    TRADERS = 'TR'
    GUILDMASTERS = 'GM'
    QUESTGIVERS = 'QG'
    BLACKSMITH = 'BM'
    TANNERS = 'TN'
    POTIONSMASTERS = 'PM'
    WIZRADS = 'WZ'

    CATEGORY_CHOICES = (
        (TANKS, 'Танки'),
        (HEALERS, 'Хилы'),
        (DAMAGEDEALER, 'ДД'),
        (TRADERS, 'Торговцы'),
        (GUILDMASTERS, 'Гилдмастеры'),
        (QUESTGIVERS, 'Квестгиверы'),
        (BLACKSMITH, 'Кузнецы'),
        (TANNERS, 'Кожевники'),
        (POTIONSMASTERS, 'Зельевары'),
        (WIZRADS, 'Мастера Заклинаний'),
    )

    name = models.CharField(
        max_length=2, choices=CATEGORY_CHOICES, default=GUILDMASTERS, unique=True)

    def get_category(self):
        return self.name

    def __str__(self) -> str:
        return self.name


class Post(models.Model):

    SELL = 'SL'
    BUY = 'BY'
    CHANGE = 'CH'
    CATEGORY_CHOICES = (
        (SELL, 'Продать'),
        (BUY, 'Купить'),
        (CHANGE, 'Обменять'),

    )

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    postType = models.CharField(
        max_length=2, choices=CATEGORY_CHOICES, default=SELL)
    postCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    dateCreation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    text = models.TextField()
    image = models.ImageField(upload_to='images/%Y-%m-%d/')
    video = models.FileField(upload_to='videos/%Y-%m-%d/')
    files = models.FileField(upload_to='files/%Y-%m-%d/')

    def preview(self):
        return self.text[:124] + '...'

    def __str__(self) -> str:
        return f'{self.title} {self.preview()}'

    # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с постом
    def get_absolute_url(self):
        return f'/post/{self.id}'

    def save(self, *args, **kwargs):
        # сначала вызываем метод родителя, чтобы объект сохранился
        super().save(*args, **kwargs)
        # затем удаляем его из кэша, чтобы сбросить
        cache.delete(f'post-{self.pk}')

# отклик


class Feedback(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
