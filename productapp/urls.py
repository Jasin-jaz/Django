from django.urls import path
from productapp.views import *
urlpatterns=[
    path('category/',category_list,name='category_list'),
    path('product/',product_list,name='product_list'),
    path('product/variants/',productvar_list,name='productvar_list'),
    path('category/<int:category_id>/view',category_view,name='category_view'),
    path('product/<int:product_id>/view',product_view,name='product_view'),
    path('product/variants/<int:productvar_id>/view',productvar_view,name='productvar_view'),
    path('category/<int:category_id>/products/',CategoryWithProduct.as_view(),name='category-with-product'),


    # path('category/<int:category_id>/delete',category_delete,name='category_delete'),
    # path('product/<int:product_id>/delete',product_delete,name='product_delete'),
    # path('category/<int:category_id>/edit',category_edit,name='category_edit'),
    # path('product/<int:product_id>/edit',product_edit,name='product_edit'),
    # path('category/<int:category_id>/update',category_update,name='category_update'),
    # path('product/<int:product_id>/update',product_update,name='product_update'),
    # path('category/<int:category_id>/products/',CategoryWithProduct.as_view(),name='category-with-product'),
]
