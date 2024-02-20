from django.urls import path
from . import views


urlpatterns = [
    path('' , views.home),
    path('logout',views.logout_view),
    path('create/', views.G_auth_api, name='my-model-create'),



]