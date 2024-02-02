from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from ext.auth import BaseAuthentication


# Create your views here.

class HomeView(APIView):
    authentication_classes = []

    def get(self, request):
        return Response("...")