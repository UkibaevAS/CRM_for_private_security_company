from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from CRM_PSC.worker.models import Worker


class Number_Of_Empoyees(APIView):
    def get(self, request: Request) -> Response:
        queryset = Worker.objects.all()