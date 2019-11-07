from django.urls import path

from .views import (
	partner_detail_view,
	partner_list_view, 
	partner_update_view,
	partner_delete_view
	)

urlpatterns = [
    path('', partner_list_view),
    path('<int:id>/', partner_detail_view),
    path('<int:id>/edit/', partner_update_view),
    path('<int:id>/delete/', partner_delete_view),
]
