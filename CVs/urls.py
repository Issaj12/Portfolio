from  django.urls import path
from about.views import about_cvs, cv_detail
urlpatterns = [
    path('', about_cvs, name='cv_list'),
    path('<int:cv_id>/', cv_detail, name='cv_detail'),
]