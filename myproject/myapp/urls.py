from django.urls import path
from . import views
app_name = 'myapp'
urlpatterns = [
    # post views
    path('', views.data_list, name='data_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail, name='post_detail'),
    path('<int:post_id>/share/',
         views.post_share, name='post_share'),
]