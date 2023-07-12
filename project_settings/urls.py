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
    path("afra/",views.afra,name="afra"),
    path("dessert/",views.dessert,name="dessert"),
    path("gt/",views.gt,name="gt"),
    path("robtech/",views.robtech,name="robtech"),
    path("ba_properties/",views.ba_properties,name="ba_properties"),
    path("demo1/",views.demo1,name="demo1"),
    path("demo2/",views.demo2,name="demo2"),
]
