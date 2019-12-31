from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from todos import views
 
urlpatterns = [
    url('todos/$', views.TodoList.as_view(), name='todo-list'),
    url('todos/(?P<pk>[0-9]+)/$', views.TodoDetail.as_view(), name='todo-detail'),
]