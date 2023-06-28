from rest_framework import serializers
from django.contrib.auth.models import User

from .models import News, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username',]


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True,)
    class Meta:
        model = Comment
        fields = ['id', 'date', 'text', 'news', 'author',]

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)


class NewsSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True,)
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = News
        fields = ['id', 'date', 'title', 'text', 'author', 'likes', 'comments']
    
    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)
