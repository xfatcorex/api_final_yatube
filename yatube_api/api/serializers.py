import base64

from django.core.files.base import ContentFile
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import (CurrentUserDefault, ImageField,
                                        ModelSerializer, ValidationError)
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class Base64ImageField(ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return super().to_internal_value(data)


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(
        slug_field='username', read_only=True)
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')
        model = Post


class GroupSerializer(ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment
        read_only_fields = ('post',)


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(
        read_only=True, slug_field='username',
        default=CurrentUserDefault()
    )

    following = SlugRelatedField(
        queryset=User.objects.all(), slug_field='username')

    class Meta:
        fields = ('user', 'following')
        model = Follow

        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]

    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise ValidationError(
                'Нельзя подписаться на самого себя'
            )
        return data
