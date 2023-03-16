from django.urls import path
from .controller import authview
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('', views.landingpage, name="landingpage"),
    path('add_product/', views.addProduct, name='addProduct'),
    path('edit_product/<str:pk>', views.editProduct, name='editProduct'),
    path('delete_product/<str:pk>', views.deleteProduct, name='deleteProduct'),

    path('login/', authview.loginpage, name='loginpage'),
    path('logout/', authview.logoutpage, name='logoutpage'),
    path('register/', authview.register, name='register'),

]

handler404 = 'dezi.views.handling_404'
