
from .views import import_records, list_records, get_record
from django.urls import path


urlpatterns = [
    path('import/', import_records, name='import'),
    path('detail/<str:model_name>/', list_records, name='record-list'),
    path('detail/<str:model_name>/<int:pk>/', get_record, name='record-detail'),
]
