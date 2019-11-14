from django.urls import path
from .views import (
    blog_post_detail_view,
    blog_post_list_view,
    objects_list_view,
    objects_create_view,
    deal_create_view,
    deal_product_create_view,
    objects_update_view,
    objects_delete_view,
    deal_list_view,
    blog_post_update_view,
    blog_post_delete_view,
    generate_report_view,
    verify_signatyre_view
)

urlpatterns = [
    path('', blog_post_list_view),
    path('deal/', deal_list_view),
    path('deal/new/', deal_create_view),
    path('deal/generate_report/', generate_report_view),
    path('deal/verify_signature/', verify_signatyre_view),
    path('deal/<int:id>/new-product/', deal_product_create_view),
    path('<str:object_name>/', objects_list_view),
    path('<str:object_name>/new/', objects_create_view),
    path('<str:object_name>/<int:id>/edit/', objects_update_view),
    path('<str:object_name>/<int:id>/delete/', objects_delete_view),
    path('blog/<str:slug>/', blog_post_detail_view),
    path('blog/<str:slug>/edit/', blog_post_update_view),
    path('blog/<str:slug>/delete/', blog_post_delete_view),
]
