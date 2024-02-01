from django.db import models

# 데이터베이스의 테이블. 사용자의 정보를 담을 수 있는 필드 선언.
# Create your models here.
class Profile(models.Model):
    name = models.TextField(null=True)
    posts = models.TextField(null=True) # IntegerField
    followers = models.TextField(null=True)
    following = models.TextField(null=True)

    # def __str__(self):
    #     return self.name
    
class Post(models.Model):
    profile = models.ForeignKey(Profile, related_name='post', null=True, on_delete=models.CASCADE) #CASCADE
    date = models.IntegerField(null=True)
    like = models.IntegerField(null=True) # IntegerField
    content = models.TextField(null=True)
    tags = models.TextField(null=True, blank=True) # 해시태그가 없는 게시물은 빈칸으로 채워넣기 위해 blank=True

    # def __str__(self):
    #     return self.date