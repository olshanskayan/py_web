from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
# router.register(r'mix/', views.BlogViewMix)

app_name = 'blog'
# urlpatterns = [
#     path('', views.BlogListView.as_view(), name='blog-list'),
#     path('mix/', views.BlogViewMix.as_view(), name='blog-mix'),
#     path('', include(router.urls))
# ]


# urlpatterns = [
#     path('notes/', views.NotesView.as_view(), name='notes'),
#     path('note/<int:note_id>/', views.NoteDetailView.as_view(), name='note'),
#     path('note/add/', views.NoteEditorView.as_view(), name='add'),
#     path('note/<int:note_id>/save/', views.NoteEditorView.as_view(), name='save'),
#     ]

urlpatterns = [
    path('notes/', views.NotesView.as_view(), name='notes'),
    path('note/<int:note_id>/', views.NoteDetailView.as_view(), name='note'),
    path('note/add/', views.NoteEditorView.as_view(), name='add'),
    path('note/<int:note_id>/save/', views.NoteEditorView.as_view(), name='save'),

    path('comment/<int:note_id>/add/', views.CommentDetailView.as_view(), name='comment_add'),
    path('comment/<int:comment_id>/del/', views.CommentDetailView.as_view(), name='comment_del'),

]