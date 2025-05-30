from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecordListView.as_view(), name='record_list'),
    path('record/create/', views.RecordCreateView.as_view(), name='record_create'),
    path('record/<int:pk>/edit/', views.RecordUpdateView.as_view(), name='record_edit'),
    path('record/<int:pk>/delete/', views.RecordDeleteView.as_view(), name='record_delete'),

    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    path('subcategory/', views.SubcategoryListView.as_view(), name='subcategory_list'),
    path('subcategory/create/', views.SubcategoryCreateView.as_view(), name='subcategory_create'),
    path('subcategory/<int:pk>/edit/', views.SubcategoryUpdateView.as_view(), name='subcategory_edit'),
    path('subcategory/<int:pk>/delete/', views.SubcategoryDeleteView.as_view(), name='subcategory_delete'),

    path('type/', views.TypeListView.as_view(), name='type_list'),
    path('type/create/', views.TypeCreateView.as_view(), name='type_create'),
    path('type/<int:pk>/edit/', views.TypeUpdateView.as_view(), name='type_edit'),
    path('type/<int:pk>/delete/', views.TypeDeleteView.as_view(), name='type_delete'),

    path('status/', views.StatusListView.as_view(), name='status_list'),
    path('status/create/', views.StatusCreateView.as_view(), name='status_create'),
    path('status/<int:pk>/edit/', views.StatusUpdateView.as_view(), name='status_edit'),
    path('status/<int:pk>/delete/', views.StatusDeleteView.as_view(), name='status_delete'),
]
