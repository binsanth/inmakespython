from . import views
from django.urls import path

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('list/',views.tasklist.as_view(),name='list'),
    path('detail/<int:pk>/',views.detailview.as_view(),name='detail'),
    path('updateview/<int:pk>/',views.updateview.as_view(),name='updateview'),
    path('deleteview/<int:pk>/',views.detailview.as_view(),name='deleteview')

]