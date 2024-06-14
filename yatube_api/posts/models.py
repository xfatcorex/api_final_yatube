from django.contrib.auth import get_user_model
from django.db import models

TEXT_LENGTH = 50

User = get_user_model()


class Post(models.Model):
    text = models.TextField('Текст публикации')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Автор публикации')
    image = models.ImageField('Фото',
                              upload_to='posts/', blank=True)
    group = models.ForeignKey(
        'Group', on_delete=models.SET_NULL,
        blank=True, null=True, verbose_name='Группа'
    )

    class Meta:
        default_related_name = 'posts'
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.text[:TEXT_LENGTH]


class Group(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('Идентификатор', unique=True)
    description = models.TextField('Описание')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Автор комментария')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        verbose_name='Публикация')
    text = models.TextField('Текст комментария')
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        default_related_name = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:TEXT_LENGTH]


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='users', verbose_name='Пользователь')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='follows', verbose_name='Подписка')

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_user_following'
            )
        ]

    def __str__(self):
        return f'{self.user} - {self.following}'
