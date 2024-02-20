from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProfileSerializer, PostSerializer, ReelsSerializer
from .models import Profile, Post, Reels
from django.http import JsonResponse
import crawling

# 화면을 작성하는 메인 뷰
# views: 요청을 받아 요청에 대한 응답을 제공하는 기능.
# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all() # 모델에 존재하는 테이블의 데이터를 전부 가져옴. SQL의 select * from Item에 해당.
    serializer_class = ProfileSerializer # 이전에 생성한 ProfileSerializer 클래스를 사용.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all() # 모델에 존재하는 테이블의 데이터를 전부 가져옴. SQL의 select * from Item에 해당.
    serializer_class = PostSerializer # 이전에 생성한 PostSerializer 클래스를 사용.

class ReelsViewSet(viewsets.ModelViewSet):
    queryset = Reels.objects.all() # 모델에 존재하는 테이블의 데이터를 전부 가져옴. SQL의 select * from Item에 해당.
    serializer_class = ReelsSerializer # 이전에 생성한 ReelsSerializer 클래스를 사용.

def crawling_method(request):
    username = request.GET.get('input_data', '')
    return JsonResponse(crawling.insta_crawling(username))