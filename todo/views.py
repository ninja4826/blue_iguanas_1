from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from todo.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing and editing users.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing and editing groups.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer