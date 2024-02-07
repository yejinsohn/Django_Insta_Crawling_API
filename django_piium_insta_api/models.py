from django.db import models

# 데이터베이스의 테이블. 사용자의 정보를 담을 수 있는 필드 선언.
# Create your models here.
class Profile(models.Model):
    name = models.TextField(null=True) # 인스타 계정명
    posts = models.IntegerField(null=True) # 인스타 게시물 수
    followers = models.IntegerField(null=True) # 인스타 팔로워 수
    following = models.IntegerField(null=True) # 인스타 팔로잉 수

    # def __str__(self):
    #     return self.name
    
class Post(models.Model):
    profile = models.ForeignKey(Profile, related_name='post', null=True, on_delete=models.CASCADE)
    date = models.IntegerField(null=True) # 인스타 게시물 업로드 날짜
    like = models.IntegerField(null=True) # 인스타 게시물 좋아요 수
    content = models.TextField(null=True) # 인스타 게시물 본문
    tags = models.TextField(null=True, blank=True) # 인스타 게시물 해시태그
    tag_length = models.IntegerField(null=True) # 인스타 게시물 해시태그 개수
    comment_most_like = models.TextField(null=True) # 인스타 게시물 댓글 내 좋아요를 많이 받은 댓글

    # def __str__(self):
    #     return self.date