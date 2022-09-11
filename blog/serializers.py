from rest_framework import serializers
from .models import Blog


# class BlogSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     slug = serializers.SlugField()

#     # TODO
#     # author =

#     content = serializers.CharField()
#     is_active = serializers.BooleanField()

#     def create(self, validated_data):
#         obj = Blog.objects.create(**validated_data)
#         obj.save()
#         return obj

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.slug = validated_data.get('slug', instance.slug)
#         instance.content = validated_data.get('content', instance.content)
#         instance.is_active = validated_data.get('is_active', instance.is_active)
#         instance.save()
#         return instance


class BlogSerializer(serializers.ModelSerializer):
    class Meta:



        model = Blog
        fields = ["id", "title", "slug", "content", "is_active"]
