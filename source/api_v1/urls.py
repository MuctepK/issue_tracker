from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api_v1.views import IssueViewSet, ProjectViewSet, LogoutView, RegisterView

router = routers.DefaultRouter()
router.register(r'issues', IssueViewSet)
router.register(r'projects', ProjectViewSet)
app_name = 'api_v1'
urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='obtain_auth_token'),
    path('logout/', LogoutView.as_view(), name='delete_auth_token'),
    path('register/', RegisterView.as_view(), name='register_view')
]
