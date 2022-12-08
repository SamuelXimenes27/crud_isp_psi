# envia
from django.contrib import admin
from django.urls import path
from app.views import home, form, create, edit, update, delete, formOS, createOS, editOS, updateOS, deleteOS, dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('formOS/', formOS, name='formOS'),
    path('createOS/', createOS, name='createOS'),
    path('editOS/<int:pk>/', editOS, name='editOS'),
    path('updateOS/<int:pk>/', updateOS, name='updateOS'),
    path('deleteOS/<int:pk>/', deleteOS, name='deleteOS'),

]
