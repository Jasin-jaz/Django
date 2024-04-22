from django.urls import path
from deliveryapp.views import *
urlpatterns=[
		path('delivery_list',delivery_list, name='delivery'),
		path('order/list', OrderList.as_view(), name='order-list'),
    	path('order/add/', OrderAdd.as_view(), name='order-add'),
    	path('order/<int:order_id>/edit/', OrderEdit.as_view(), name='order-edit'),	
]