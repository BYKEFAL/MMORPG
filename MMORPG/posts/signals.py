from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Post
from django.conf import settings


@receiver(m2m_changed, sender=Post.respondent.through)
def response_add_post(sender, instance, action, **kwargs):

    # Добавился отклик
    if action == 'post_add':
        user_of_current_post = instance.author
        feedback = instance.respondent.last()
        html = render_to_string(
            'mailing/new_response_notification.html',
            {
                'post': instance,
                'feedback': feedback
            },
        )

        msg = EmailMultiAlternatives(
            subject=f'Здравствуй, {user_of_current_post.username}. Новый отклик на вашу публикацию',
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user_of_current_post.email,],
            # to=[settings.MY_TEST_EMAIL,],
        )

        msg.attach_alternative(html, 'text/html')
        try:
            msg.send()
        except Exception as e:
            print(e)
