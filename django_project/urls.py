from django.contrib import admin
from django.urls import path, include

app_name = "pages"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
]
