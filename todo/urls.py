from todo.views import UserViewSet, TaskList, TaskDetail
from rest_framework import renderers

user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_me = UserViewSet.as_view({
    'get': 'me'
}, renderer_classes=[renderers.JSONRenderer])

task_list = TaskList.as_view()

task_detail = TaskDetail.as_view()