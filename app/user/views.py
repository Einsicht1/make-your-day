import requests

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

from user.serializers import UserSerializer, SocialUserSerializer
from django.contrib.auth import get_user_model


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter


class KakaoSignUpView(APIView):
    """kakao signup view"""

    def post(self, request):
        access_token = request.headers.get("Authorization", None)
        print("access_token:", access_token)
        profile_request = requests.post(
            "https://kapi.kakao.com/v2/user/me",
            # "https://kapi.kakao.com/v1/user/logout",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        if profile_request.status_code != 200:
            return Response("INVALID_TOKEN", status=status.HTTP_401_UNAUTHORIZED)
        profile_json = profile_request.json()
        # print(profile_json)
        kakao_user_exists = get_user_model().objects.filter(social_platform='kakao',
                                                            social_id=profile_json['id']
                                                            ).exists()
        print(kakao_user_exists)

        if not kakao_user_exists:
            print("not exists")
            user = get_user_model().objects.create(username=profile_json['properties']['nickname'],
                                                   social_platform='kakao',
                                                   social_id=profile_json['id'],
                                                   thumbnail_image=profile_json['properties']['thumbnail_image'])
        else:
            print('exists')
            user = get_user_model().objects.get(social_platform='kakao',
                                                social_id=profile_json['id']
                                                )

        serializer = SocialUserSerializer(data=user)
        user_data = serializer.get_user_data(user)
        print(user_data)

        from rest_framework_jwt.settings import api_settings
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        print(token)

        return Response(user_data, status=status.HTTP_200_OK)
