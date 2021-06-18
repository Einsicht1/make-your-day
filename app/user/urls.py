from django.urls import path

from user import views


app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('rest-auth/kakao/', views.KakaoLogin.as_view(), name='kakao-login'),
    path('kakao-test/', views.KakaoSignUpView.as_view(), name='kakao-test'),
]