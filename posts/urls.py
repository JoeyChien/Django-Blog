from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name = 'index' ),
    path('create', views.post_create_view, name = 'create' ),
    path('<int:id>/', views.singlePost, name = 'post_id' ),

]
