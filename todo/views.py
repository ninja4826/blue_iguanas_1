from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from todo.models import Task
from todo.serializers import UserSerializer, TaskSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing and editing users.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    
    @detail_route(renderer_classes=[JSONRenderer])
    def me(self, request, *args, **kwargs):
        return Response(UserSerializer(request.user, context={'request':request}).data)

class TaskList(APIView):
    """
    List current user's tasks, or create a new task.
    """
    def get(self, request, format=None):
        tasks = Task.objects.filter(user_id=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        old_task = request.data
        
        old_task['user_id'] = request.user.id
        serializer = TaskSerializer(data=old_task)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)