from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
 
from auth_api import views
urlpatterns = [
    url('admin/', admin.site.urls),
    url('docs/', include_docs_urls(title='Todo API', description='RESTful API for Todo')),
 
    url('$', views.api_root),
    url('', include(('users.urls', 'users'), namespace='users')),
    url('', include(('todos.urls', 'todos'), namespace='todos')),
]