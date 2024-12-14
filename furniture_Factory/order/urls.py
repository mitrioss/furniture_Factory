from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    # Путь для списка цехов
    path('list_order', views.OrderListView.as_view(), name='list_order'),

    # Путь для карточки цеха
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='detail_order'),

    # Путь для создания нового цеха
    path('order/create/', views.OrderCreateView.as_view(), name='create_order'),

    # Путь для редактирования цеха
    path('order/<int:pk>/edit/', views.OrderUpdateView.as_view(), name='edit_order'),

    # Путь для удаления цеха
    path('order/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='delete_order')
]
