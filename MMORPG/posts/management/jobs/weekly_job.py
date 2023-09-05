from datetime import timedelta
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from posts.models import *
from django.conf import settings


def compose_obj(post):
    _post = {}
    _post['id'] = post.id
    _post['title'] = post.title
    return _post


def send_notification(user, cat_obj):
    subject = f'Еженедельная рассылка новых публикаций'

    posts_info = {"category": '', "posts": []}

    for category, posts in cat_obj.items():
        posts_info["category"] = category
        posts_info["posts"] = [compose_obj(post) for post in posts]

    html = render_to_string(
        'mailing/weekly_notification.html',
        {
            'user_name': user,
            'posts_info': posts_info,
        },
    )

    msg = EmailMultiAlternatives(
        subject=subject,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email, ],
    )
    msg.attach_alternative(html, "text/html")
    msg.send()


def weelky_news_job():
    for category in Category.objects.all():
        mailing_dict = {}  # инициализация переменной, пустой словарь <class 'dict'>
        cat_name = category.name
        postsForWeek = Post.objects.filter(
            postCategory=category, dateCreation__gte=timezone.now() - timedelta(weeks=1))
        if not postsForWeek:
            continue
            # вычисляем юзеров-подписчиков
        for user in User.objects.all():
            if user not in mailing_dict:

                mailing_dict[user] = {}

            if cat_name not in mailing_dict[user]:
                mailing_dict[user][cat_name] = set()

            mailing_dict[user][cat_name].update(postsForWeek)

        for user, cat_name in mailing_dict.items():
            send_notification(user, cat_name)
