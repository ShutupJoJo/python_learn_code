from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'front'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('message', views.MessageView.as_view(), name='message'),
    path('user/info', views.UserInfoView.as_view(), name='user_info'),
    path('login', views.LoginView.as_view(), name='login')
]

router = DefaultRouter()
router.register('user', views.AsyncUserViewSet, basename='user')
urlpatterns += router.urls