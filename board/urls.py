
from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('list/', views.ListView.as_view(), name='list'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update')
]
