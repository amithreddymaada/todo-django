from django.urls import path
from django.shortcuts import reverse
from .views import (
    RemainderListView,
    RemainderDetailView,
    RemainderCreateView,
    RemainderUpdateView,
    RemainderDeleteView,
    UserRemainderListView
)
from . import views

urlpatterns=[
    path('',RemainderListView.as_view(),name='index'),
    path('user/<str:username>/',UserRemainderListView.as_view(),name='user-remainders'),
    path('remove_outdated/',views.remove_outdated,name='remove_outdated'),
    path('<int:pk>/detail/',RemainderDetailView.as_view(),name='detail'),
    path('create/',RemainderCreateView.as_view(),name='create'),
    path('<int:pk>/update/',RemainderUpdateView.as_view(),name='update'),
    path('<int:pk>/delete/',RemainderDeleteView.as_view(),name='delete'),
    # path('',views.remainderlistview,name='index'),
]