# Generated by Django 4.2.4 on 2023-08-30 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_author_alter_post_posttype_delete_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postType',
            field=models.CharField(choices=[('TK', 'Танки'), ('HL', 'Хилы'), ('DD', 'Даммагеры'), ('TR', 'Торговцы'), ('GM', 'Гилдмастеры'), ('QG', 'Квестгиверы'), ('BM', 'Кузнецы'), ('TN', 'Кожевники'), ('PM', 'Зельевары'), ('WZ', 'Мастера Заклинаний')], max_length=2),
        ),
    ]