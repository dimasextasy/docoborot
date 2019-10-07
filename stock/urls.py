from django.urls import path

from .views import (
	stock_item_detail_view,
	stock_item_list_view, 
	stock_item_update_view,
	stock_item_delete_view
	)

urlpatterns = [
    path('', stock_item_list_view),
    path('<str:slug>/', stock_item_detail_view),
    path('<str:slug>/edit/', stock_item_update_view),
    path('<str:slug>/delete/', stock_item_delete_view),
]
