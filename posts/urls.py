from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.post_create_view),
    path('<int:id>/', views.singlePost, name = 'post_id' ),

]
