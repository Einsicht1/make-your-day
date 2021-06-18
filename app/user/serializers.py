from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'username')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)


class SocialUserSerializer(serializers.ModelSerializer):
    """Serializer for social login user object"""

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'thumbnail_image')

    def get_user_data(self, user):
        res = {
            'token': 'this is JWT token',
            'user': {
                'pk': user.id,
                'username': user.username,
                'thumnail_url': user.thumbnail_image
            }
        }
        return res
