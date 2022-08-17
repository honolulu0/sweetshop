from django.urls import path
from sweetapp.views import *

urlpatterns = [
    path('products/', ProductListView.as_view(), name='ProductListView'),
    path('products_page/', ProductListPageView.as_view(), name='ProductListPageView'),
    path('create_product/', CreateProductView.as_view(), name='CreateProductView'),
    path('products/delete_product/', DeleteProductView.as_view(), name='DeleteProductView'),
    path('products/update_product/', UpdateProductView.as_view(), name='UpdateProductView'),

    path('users/', UserListView.as_view(), name='UserListView'),
    path('user/', UserView.as_view(), name='UserView'),

    path('users/create_user/', CreateUserView.as_view(), name='CreateUserView'),
    path('users/update_user/', UpdateUserView.as_view(), name='UpdateUserView'),

    path('users/delete_user/', DeleteUserView.as_view(), name='DeleteUserView'),

    path('notice/', NoticeView.as_view(), name='NoticeView'),
    path('notice/update_notice/', NoticeView.as_view(), name='NoticeView'),

]
