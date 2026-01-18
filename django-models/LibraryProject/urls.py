from django.contrib import admin
from django.urls import path, include
from relationship_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')), 
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    ]