from django.urls import path
from .views import SemListView,SemCreateView,SemUpdateView
from . import views
urlpatterns=[
    path('',SemListView.as_view(),name='sem-index'),
    path('create/',SemCreateView.as_view(),name='sem-create'),
    path('<int:sem>/marks/',views.sem_marks,name='sem-marks'),
    path('<int:pk>/update/',SemUpdateView.as_view(),name='sem-update'),
    # path('<int:id>/update/',views.sem_update,name='sem-update'),
]