from django.urls import include
from django.urls import path
from . import views

# urlpatterns += [
#     path('mgmt/', include('mgmt.urls')),
# ]

urlpatterns = [
    path('', views.home, name='home'),
    path('list_clients', views.list_clients, name='list-clients'),
    path('list_massages', views.list_massages, name='list-massages'),
    path('list_services', views.list_services, name='list-services'),
    path('add_client', views.add_client, name='add-client'),
    path('add_service', views.add_service, name='add-service'),
    path('show_client/<int:client_id>', views.show_client, name='show-client'),
]
