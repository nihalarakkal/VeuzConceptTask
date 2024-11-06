from django.urls import path
from Employee import views

urlpatterns=[
    path('index_page/',views.index_page,name="index_page"),
    path('register_page/',views.register_page,name="register_page"),
    path('login_page/',views.login_page,name="login_page")
]