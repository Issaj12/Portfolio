from django.urls import path
from . import views

urlpatterns = [



    # Public view (users only view)
    path('', views.work_list, name='list'),
    path('<int:pk>/', views.work_detail, name='work_detail'),
]

