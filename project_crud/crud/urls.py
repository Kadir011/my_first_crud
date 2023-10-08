from django.urls import path 
from django.contrib.auth import views as auth_views 
from . import views 
from django.conf import settings 
from django.contrib.staticfiles.urls import static 

urlpatterns = [ 
    path('', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('inicio', views.inicio, name='inicio'),
    path('info', views.info, name='info'),  
    path('libros', views.libros, name='libros'), 
    path('libros/crear', views.crear, name='crear'), 
    path('libros/edicion/<id>', views.edicion, name='edicion'),
    path('editar', views.editar, name='editar'),
    path('eliminar/<id>', views.eliminar, name='eliminar'), 
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 












