from django.urls import path
from .views import dashboard, admin_login, admin_panel, post_notice, delete_notice, update_notice

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('custom-admin/login/', admin_login, name='admin_login'),
    path('custom-admin/panel/', admin_panel, name='admin_panel'),
    path('custom-admin/post/', post_notice, name='post_notice'),

    path('custom-admin/delete/', delete_notice, name='delete_notice'),
    path('custom-admin/update/', update_notice, name='update_notice'),
]
