from rest_framework import serializers
from .models import Profile, Post, Reels # 선언한 모델 import

# serializer: Django 프로젝트에서 모델로부터 뽑은 queryset을 Json타입으로 바꾸는 직렬화 기능.
# ModelSerializer: Model에 정의한 필드에 해당하는 값을 Serializer에서 사용 가능.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("__all__")
        # fields = ('date', 'like', 'content', 'tags')

class ReelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reels
        fields = ("__all__")

class ProfileSerializer(serializers.ModelSerializer):
    post = PostSerializer(many=True)
    reels = ReelsSerializer(many=True)
    
    class Meta:
        model = Profile # 모델 설정
        fields = ("__all__") # 사용하고 싶은 필드 나열
        # fields = ('posts', 'followers', 'following', 'post')

    def create(self, validated_data):
        posts_data = validated_data.pop('post')
        reelses_data = validated_data.pop('reels')
        profile = Profile.objects.create(**validated_data) # Profile데이터
        for post_data in posts_data:
            Post.objects.create(profile = profile, **post_data) # Post데이터

        for reels_data in reelses_data:
            Reels.objects.create(profile = profile, **reels_data) # Reels데이터

        return profile