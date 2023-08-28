from django.urls import path

from .views import (
    ClientListView,
    PerformerListView,
    PostListView,
    Protected_objectListView,
)

app_name = 'protected_object'



urlpatterns = [
    path('client/', ClientListView.as_view(), name='clients'),
    path('performer/', PerformerListView.as_view(), name='performers'),
    path('post/', PostListView.as_view(), name='posts'),
    path('protected_object/', Protected_objectListView.as_view(), name='protected_objects'),
]
