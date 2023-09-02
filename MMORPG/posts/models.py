from django.db import models
from django.contrib.auth.models import User
from django.core.cache import cache


class Category(models.Model):

    name = models.CharField(max_length=64, unique=True)

    def get_category(self):
        return self.name

    def __str__(self) -> str:
        return self.name


class Feedback(models.Model):
    feedbackUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Отклик-{self.feedbackUser} №{self.pk}'


class Post(models.Model):
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
        (DAMAGEDEALER, 'Даммагеры'),
        (TRADERS, 'Торговцы'),
        (GUILDMASTERS, 'Гилдмастеры'),
        (QUESTGIVERS, 'Квестгиверы'),
        (BLACKSMITH, 'Кузнецы'),
        (TANNERS, 'Кожевники'),
        (POTIONSMASTERS, 'Зельевары'),
        (WIZRADS, 'Мастера Заклинаний'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    postType = models.CharField(
        max_length=2, choices=CATEGORY_CHOICES)
    postCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    dateCreation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    text = models.TextField()
    image = models.ImageField(upload_to='images/%Y-%m-%d/')
    respondent = models.ManyToManyField(Feedback, through='FeedBackMany')

    def preview(self):
        return self.text[:124] + '...'

    def __str__(self) -> str:
        return f'{self.title}'

    # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с постом
    def get_absolute_url(self):
        return f'/posts/{self.id}'

    def save(self, *args, **kwargs):
        # сначала вызываем метод родителя, чтобы объект сохранился
        super().save(*args, **kwargs)
        # затем удаляем его из кэша, чтобы сбросить
        cache.delete(f'post-{self.pk}')

# отклик


class FeedBackMany(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    respondentThrough = models.ForeignKey(Feedback, on_delete=models.CASCADE)
