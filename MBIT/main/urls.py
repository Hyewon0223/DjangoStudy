from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('submit/', views.submit, name='submit'),
    path('result/<int:developer_id>', views.result, name='result'),
    path('all_results/', views.all_results, name='all_results'),
]
