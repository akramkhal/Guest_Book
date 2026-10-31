from django.urls import path
from webapp.views import index_view, guest_add_view

urlpatterns = [
    path('', index_view, name='index'),
    path('guest/add', guest_add_view, name='guest_add'),
]
