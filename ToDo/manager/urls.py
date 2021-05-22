from django.urls import path
from . import views
urlpatterns = [path('',views.home,name='home'),
               path('show',views.products,name='products'),
               path('update/<int:sno>',views.update,name='update'),
               path('delete/<int:sno>',views.delete,name='delete')]