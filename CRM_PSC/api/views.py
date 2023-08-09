from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# from CRM_PSC.api.serializers import WorkerSerializer
from worker.models import Worker
from api.serializers import WorkerSerializer


@api_view()
def hello_view(request: Request) -> Response:
    return Response({'message': 'Hi'})


# class NumberEmployees(ListModelMixin, GenericAPIView):
#     queryset = Worker.objects.all()
#     serializer_class = WorkerSerializer
#     def get(self, request: Request) -> Response:
#         return self.list(request)

class NumberEmployeesViewSet(ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    filter_backends = [
        SearchFilter,
        #DjangoFilterBackend,
    ]
    search_fields = ['second_name']

    # filterset_fields = [
    #     'second_name',
    #     'official_employment',
    #     'organization',
    #     'category',
    #     'electrical_safety_qualification',
    # ]
