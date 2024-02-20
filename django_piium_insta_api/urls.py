from django.urls import include, path
from rest_framework import routers
from . import views #views.py import

router = routers.DefaultRouter() #DefaultRouter를 설정
router.register('Profile', views.ProfileViewSet) #ProfileViewSet 과 Profile이라는 router 등록
router.register('Post', views.PostViewSet) #PostViewSet 과 Post router 등록
router.register('Reels', views.ReelsViewSet) #ReelsViewSet 과 Reels router 등록

urlpatterns = [
    path('', include(router.urls)),
    path('crawling_method/', views.crawling_method)
]