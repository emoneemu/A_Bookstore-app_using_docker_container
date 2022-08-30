from django.contrib import admin
from django.urls import path, include

app_name = "pages"
urlpatterns = [
    # django admin
    path("admin/", admin.site.urls),
    # django user manager
    path("accounts/", include("django.contrib.auth.urls")),
    # django Local apps
    path("accounts/", include("accounts.urls")),
    path("", include("pages.urls")),
]
