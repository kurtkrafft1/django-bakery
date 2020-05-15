from django.urls import path
from .views import *

app_name = "breadapp"

urlpatterns = [
    path('', bread_list, name="breads"),
    path('new/', bread_form, name="bread_form"),
    path('bread/<int:bread_id>/', bread_details, name="bread_details"),
    path('bread/edit/<int:bread_id>/', bread_edit_form, name="bread_edit_form"),
]
