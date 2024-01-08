from django.urls import path, include 
from django.contrib import admin 
from .views import dashboard, profile_list, profile
from dwitter import views
from django.conf.urls.static import static
from django.conf import settings 

app_name = "dwitter"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"), 
    path("dweets/<int:image_id>", views.Dweet),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 