from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = {
    path('', views.home, name='home'),
    path('signup_page', views.signup, name = 'signup')
    #path('datacollector', views.datacollector, name='datacollector')


}
