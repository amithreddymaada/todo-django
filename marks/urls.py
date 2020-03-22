from django.urls import path
from .views import SemOneListView,SemTwoListView,SemOneUpdateView,SemTwoUpdateView
from . import views
urlpatterns=[
    path('sem-one/',SemOneListView.as_view(),name='sem-one-index'),
    path('sem-two/',SemTwoListView.as_view(),name='sem-two-index'),
    path('total/',views.total_marks,name='total-index'),
    path('sem-one/<int:pk>/update/',SemOneUpdateView.as_view(),name='sem-one-update'),
    path('sem-two/<int:pk>/update/',SemTwoUpdateView.as_view(),name='sem-two-update'),

    # path('sem-one/<int:pk>/update/',)
    
]