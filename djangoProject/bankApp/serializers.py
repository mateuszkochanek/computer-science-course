from abc import ABC

from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from django.utils import timezone
from rest_framework import serializers

from bankApp.models import Transfer


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])

        if not user:
            raise serializers.ValidationError('Incorrect username or password.')

        if not user.is_active:
            raise serializers.ValidationError('User is disabled.')

        return {'user': user}


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class TransfersHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transfer
        fields = ('recipient_name', 'recipient_account', 'title', 'amount', 'date')


class TransferSendSerializer(serializers.HyperlinkedModelSerializer):
    sender = serializers.SerializerMethodField('_user')

    def _user(self, obj):
        request = getattr(self.context, 'request', None)
        if request:
            return request.user.id

    class Meta:
        model = Transfer
        fields = ('sender', 'recipient_name', 'recipient_account', 'title', 'amount')
