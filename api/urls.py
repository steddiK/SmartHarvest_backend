from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersList, ZonesList, PlantesList, DiagnosticsList, RecommandationsList

urlpatterns = [
    path('users/', UsersList.as_view(), name='users-list'),
    path('zones/', ZonesList.as_view(), name='zones-list'),
    path('plantes/', PlantesList.as_view(), name='plantes-list'),
    path('diagnostics/', DiagnosticsList.as_view(), name='diagnostics-list'),
    path('recommandations/', RecommandationsList.as_view(), name='recommandations-list'),
]

