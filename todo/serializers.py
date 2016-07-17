from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers
from todo.models import Task

User = get_user_model()

class TaskSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Task
        fields = ('id', 'user_id', 'title', 'desc', 'priority', 'created')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    tasks = serializers.SerializerMethodField()
    
    def get_tasks(self, user):
        tasks = Task.objects.filter(user_id=user.id)
        # return tasks
        return TaskSerializer(tasks, many=True, read_only=True).data
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'tasks')
        write_only_fields = ('password')
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined')
    
    def restore_object(self, attrs, instance=None):
        user = super(UserSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')