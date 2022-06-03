from django.urls import path
#
from .views import NoteListView, NoteCreateView, NoteUpdateView, delete


app_name = 'notes'
urlpatterns = [
     path('', NoteListView.as_view(), name='note_list'),
     path('create/', NoteCreateView.as_view(), name='note_create'),
     path('delete/<int:pk>/', delete, name='note_delete'),
     path('update-<int:pk>/', NoteUpdateView.as_view(), name='note_update'),
 ]
