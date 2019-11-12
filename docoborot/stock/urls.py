from django.urls import path

from .views import (
	stock_item_detail_view,
	stock_item_list_view, 
	stock_item_update_view,
	stock_item_delete_view,
	stock_item_create_view,
	partner_list_view,
	partner_detail_view
	)

urlpatterns = [
	path('stock-new/', stock_item_create_view),
    path('stock/', stock_item_list_view),
    path('stock/<str:slug>/', stock_item_detail_view),
    path('stock/<str:slug>/edit/', stock_item_update_view),
    path('stock/<str:slug>/delete/', stock_item_delete_view),
    path('partner/', partner_list_view),
    path('partner/<int:id>/', partner_detail_view)
]
