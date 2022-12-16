from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.add,name='Add'),
    path('update<int:id>',views.update,name='Update'),
    path('delete<int:id>',views.delete,name='Delete'),
]