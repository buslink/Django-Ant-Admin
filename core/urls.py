from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),

    # 自动化路由入口
    path('api/', include('autoapi.urls')),
]