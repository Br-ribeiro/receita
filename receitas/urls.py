
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('receitasapp.urls')),
    path('admin/', admin.site.urls),
]
