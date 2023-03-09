from django.contrib import admin  
from django.urls import path  
from create import views  
urlpatterns = [
     
    path('admin/', admin.site.urls),  
    path('',views.homepage),
    path('emp', views.emp),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]  