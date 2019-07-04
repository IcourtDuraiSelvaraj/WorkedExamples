from django.contrib import admin
from django.urls import path, include
from signIn import views


urlpatterns = {
    path('', include('signIn.urls')),
    path('admin/', admin.site.urls),

}
