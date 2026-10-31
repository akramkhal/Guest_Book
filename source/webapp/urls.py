from django.urls import path
from webapp.views import index_view, guest_add_view, guest_update_view, guest_delete_view

urlpatterns = [
    path('', index_view, name='index'),
    path('guest/add/', guest_add_view, name='guest_add'),
    path('guest/<int:pk>/update/', guest_update_view, name='guest_update'),
    path('guest/<int:pk>/delete/', guest_delete_view, name='guest_delete')
]
