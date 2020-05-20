from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path('<int:pk>/', views.DetailProblem.as_view(), name='detail'),
    path('add/', views.CreateProblem.as_view(), name='add'),
    path('list/', views.ListProblem.as_view(), name='list')
]

installed_apps = getattr(settings, 'INSTALLED_APPS', [])
if 'rest_framework' in installed_apps:
    from .api_views import CreateProblemAPI, RetrieveProblemAPI, ListProblemAPI

    urlpatterns += [
        path('api/add/', CreateProblemAPI.as_view(), name='api_add'),
        path('api/<int:pk>', RetrieveProblemAPI.as_view(), name='api_detail'),
        path('api/list/', ListProblemAPI.as_view(), name='api_list')
    ]
