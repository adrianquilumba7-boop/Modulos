from django.contrib import admin
from django.urls import path, include
from usuarios import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.perfil, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('', views.inicio, name='inicio'),
    path('perfil/', views.perfil, name='perfil'),
    path('modulos/', views.modulos, name='modulos'),
    path('modulo1/', views.modulo1, name='modulo1'),
    path('modulo2/', views.modulo2, name='modulo2'),
    path('modulo3/', views.modulo3, name='modulo3'),
    path('modulo4/', views.modulo4, name='modulo4'),
    path('modulo5/', views.modulo5, name='modulo5'),
    path('modulo6/', views.modulo6, name='modulo6'),
    path('modulo7/', views.modulo7, name='modulo7'),
    
    # URLs de recuperación de contraseña
    path('password_reset/', 
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset_form.html',
             email_template_name='registration/password_reset_email.html',
             subject_template_name='registration/password_reset_subject.txt',
             success_url='/password_reset/done/'
         ), 
         name='password_reset'),
    
    # Página de confirmación después de enviar el email
    path('password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ), 
         name='password_reset_done'),
    
    # ✅ URL CRÍTICA - Para el enlace del email (formato CORRECTO)
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html',
             success_url='/reset/done/'
         ), 
         name='password_reset_confirm'),
    
    # Página final después de cambiar la contraseña
    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ), 
         name='password_reset_complete'),
    
    # 🔐 URLs de LOGIN/LOGOUT (si las necesitas)
    path('login/', 
         auth_views.LoginView.as_view(
             template_name='registration/login.html'
         ), 
         name='login'),
    
    path('logout/', 
         auth_views.LogoutView.as_view(
             template_name='registration/logged_out.html'
         ), 
         name='logout'),
    
    # Página de inicio (opcional)
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]


