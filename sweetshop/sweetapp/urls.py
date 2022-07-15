from django.urls import path
from sweetapp.views import *

urlpatterns = [
    path('products/', ProductListView.as_view(), name='ProductListView'),
    path('create_product/', CreateProductView.as_view(), name='CreateProductView'),
    path('users/', UserListView.as_view(), name='UserListView'),
    path('users/create_user', CreateUserView.as_view(), name='CreateUserView'),

]
