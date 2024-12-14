from django.urls import path
from . import views

app_name = 'workshop'

urlpatterns = [
    # Путь для списка цехов
    path('', views.WorkshopListView.as_view(), name='list_workshop'),

    # Путь для карточки цеха
    path('<int:pk>/', views.WorkshopDetailView.as_view(), name='detail_workshop'),

    # Путь для создания нового цеха
    path('workshop/create/', views.WorkshopCreateView.as_view(), name='create_workshop'),

    # Путь для редактирования цеха
    path('workshop/<int:pk>/edit/', views.WorkshopUpdateView.as_view(), name='edit_workshop'),

    # Путь для удаления цеха
    path('workshop/<int:pk>/delete/', views.WorkshopDeleteView.as_view(), name='delete_workshop'),

    # Путь для списка работников
    path('workerlist/', views.WorkerListView.as_view(), name='list_worker'),

    # Путь для редактирования работников
    path('worker/<int:pk>/edit/', views.WorkerUpdateView.as_view(), name='edit_worker'),

    # Путь для создания нового работника
    path('worker/create/', views.WorkerCreateView.as_view(), name='create_worker'),

    # Путь для удаления работника
    path('worker/<int:pk>/delete/', views.WorkerDeleteView.as_view(), name='delete_worker')
]
