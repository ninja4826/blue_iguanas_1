from django.contrib.auth.models import User, Group
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from todo.models import Task
from todo.serializers import UserSerializer, TaskSerializer
from todo.permissions import IsCreateOrListUsers

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing and editing users.
    """
    permission_classes = (IsCreateOrListUsers,)
    
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
        tasks = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        old_task = request.data
        
        old_task['user'] = request.user.id
        serializer = TaskSerializer(data=old_task)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NotOwnedError(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return repr("User lacks ownership of this resource")

class TaskDetail(APIView):
    """
    Retrieve update or delete a task.
    """
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404
    
    def owned_check(self, request, task):
        return task.user.id == request.user.id
    
    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        if self.owned_check(request, task):
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        context = {
            'task_id': UserSerializer(task.user_id).data,
            'user_id': request.user.id
        }
        return Response(context, status=status.HTTP_401_UNAUTHORIZED)
    
    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        if self.owned_check(request, task):
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
            
    
    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        if self.owned_check(request, task):
            task.delete
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)