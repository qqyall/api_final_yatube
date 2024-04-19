from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
    )

    class Meta:
        model = Follow
        fields = ('id', 'user', 'following')

    validators = [
        UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=('user', 'following'),
            message='Подписка была оформлена ранее'
        )
    ]

    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError(
                'На самого себя подписаться нельзя'
            )
        return data


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group')

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'author', 'text', 'created', 'post')
        read_only_fields = ('author', 'post',)
        model = Comment
