from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("users/", include("users.urls")),
    path("",views.main,name="main"),
    path("test/",views.test,name="test"),
]
