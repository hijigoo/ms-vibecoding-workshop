from django.urls import path
from . import views

app_name = 'memos'

urlpatterns = [
    path('', views.MemoListView.as_view(), name='memo_list'),
    path('memo/<int:pk>/', views.MemoDetailView.as_view(), name='memo_detail'),
    path('memo/create/', views.MemoCreateView.as_view(), name='memo_create'),
    path('memo/<int:pk>/edit/', views.MemoUpdateView.as_view(), name='memo_update'),
    path('memo/<int:pk>/delete/', views.MemoDeleteView.as_view(), name='memo_delete'),
]
