from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('person_info/', views.person_info, name='person_info'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('calories_and_bjy/', views.calories_and_bjy, name='calories_and_bjy'),
    path('profile/', views.profile, name='profile'),
    path('report/', views.report, name='report'),
    # path('add_product/', views.add_product, name='add_product'),
]