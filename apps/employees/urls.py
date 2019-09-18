'''Urls for the employees app'''

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path(
        'employees',
        views.EmployeeListView.as_view(),
        name='employees'
    ),
    path(
        'employees/<int:pk>',
        views.EmployeeDetailView.as_view(),
        name='single-employee'
    ),
    path(
        'employee',
        views.EmployeeCreateView.as_view(),
        name='create-employee'
    ),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
