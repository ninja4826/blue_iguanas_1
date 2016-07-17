from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers
from todo.models import Task

User = get_user_model()

class TaskSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'desc', 'priority', 'completed', 'created')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    tasks = serializers.SerializerMethodField()
    
    def get_tasks(self, user):
        tasks = Task.objects.filter(user=user.id)
        # return tasks
        return TaskSerializer(tasks, many=True, read_only=True).data
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'tasks', 'password')
        # write_only_fields = ('password')
        extra_kwargs = { 'password': { 'write_only': True } }
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined')
    
    # def restore_object(self, attrs, instance=None):
    #     user = super(UserSerializer, self).restore_object(attrs, instance)
    #     user.set_password(attrs['password'])
    #     return user
    def create(self, validated_data):
        print(validated_data)
        user = User(username=validated_data['username'])
        if 'email' in validated_data:
            user.email = validated_data['email']
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    # def update(self, instance, data):
    #     instance.username = data.get('username', instance.username)
    #     instance.email = data.get('email', instance.email)
    #     return instance

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')