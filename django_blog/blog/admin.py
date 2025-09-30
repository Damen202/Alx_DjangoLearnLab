from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),   # routes requests to your users app
    path('blog/', include('blog.urls')),   # routes requests to your blog app
]
