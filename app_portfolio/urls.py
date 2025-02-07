from django.urls import path
from app_portfolio.views import *

urlpatterns = [
    path('', index_view, name='index'),
]