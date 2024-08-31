from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User


from apk.models import *
from .serializers import *


class ListView(generics.ListAPIView):

    # permission_classes = [IsAuthenticated, ]
    # authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny]
    serializer_class = CoopérativeSerializer

    def get_queryset(self):
        return Coopérative.objects.all()
        # return Coopérative.objects.filter(user=self.request.user)
