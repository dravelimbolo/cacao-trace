from rest_framework import serializers
from django.contrib.auth.models import User

from apk.models import *

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(max_length=50, required=True)
    last_name = serializers.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']


class ProducteurSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producteur
        fields = '__all__'
        # exclude = ['user', ]


class ParcelleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parcelle
        # fields = '__all__'
        exclude = ['user', ]


class CoopérativeSerializer(serializers.ModelSerializer):

    producteurs     =      ProducteurSerializer(many=True)

    class Meta:
        model = Coopérative
        # fields = '__all__'
        exclude = ['user', ]


class LotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lot
        # fields = '__all__'
        exclude = ['user', ]


class SacSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sac
        # fields = '__all__'
        exclude = ['user', ]


class AcheteurSerializer(serializers.ModelSerializer):

    class Meta:
        model = Acheteur
        # fields = '__all__'
        exclude = ['user', ]