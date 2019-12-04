from django.urls import path, include
from rest_framework import routers

from api_v1.views import IssueViewSet, ProjectViewSet

router = routers.DefaultRouter()
router.register(r'issues', IssueViewSet)
router.register(r'projects', ProjectViewSet)
app_name = 'api_v1'
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]
