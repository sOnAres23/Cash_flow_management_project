from django.urls import path
from . import views

urlpatterns = [
    path('', views.record_list, name='record_list'),  # главная страница
    path('record/create/', views.record_create, name='record_create'),
    path('record/edit/<int:pk>/', views.record_edit, name='record_edit'),
    path('record/delete/<int:pk>/', views.record_delete, name='record_delete'),

    path('category/edit/<int:pk>/', views.category_edit, name='category_edit'),
    path('category/create/', views.category_edit, name='category_create'),

    path('subcategory/edit/<int:pk>/', views.subcategory_edit, name='subcategory_edit'),
    path('subcategory/create/', views.subcategory_edit, name='subcategory_create'),

    path('type/edit/<int:pk>/', views.type_edit, name='type_edit'),
    path('type/create/', views.type_edit, name='type_create'),

    path('status/edit/<int:pk>/', views.status_edit, name='status_edit'),
    path('status/create/', views.status_edit, name='status_create'),
]
