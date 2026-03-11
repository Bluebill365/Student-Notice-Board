from django.urls import path
from .views import NoticeCreateView, NoticeListView, DashboardView

urlpatterns = [
    path('add/', NoticeCreateView.as_view(), name='notice_add'),
    path('list/', NoticeListView.as_view(), name='notice_list'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]