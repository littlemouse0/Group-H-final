
from django.urls import path
from . import views

urlpatterns = [
    path('note/<int:pk>/clone/', views.note_clone, name='note_clone'),
    path('folders/', views.folder_list, name='folder_list'),
    path('folder/<int:pk>/delete/', views.folder_delete, name='folder_delete'),
    path('folder/new/', views.folder_create, name='folder_create'),
    path('', views.note_list, name='note_list'),
    path('note/<int:pk>/', views.note_detail, name='note_detail'),
    path('note/new/', views.note_create, name='note_create'),
    path('note/<int:pk>/edit/', views.note_edit, name='note_edit'),
    path('note/<int:pk>/delete/', views.note_delete, name='note_delete'),
    path('register/', views.register, name='register'),
    path('search/', views.search_notes, name='search_notes'),
    path('note/<int:pk>/versions/', views.note_versions, name='note_versions'),
]
