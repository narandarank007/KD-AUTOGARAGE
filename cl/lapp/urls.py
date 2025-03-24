
"""
URL configuration for cl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from lapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    #--------home-------
    path('',views.home, name="home"),
    #-------sevicelogin-----------------
    #path('servicelogin',views.servicelogin,name="login"),
    path('servicelogin',auth_views.LoginView.as_view(template_name='servicelogin.html'),name="servicelogin"),
    path('servicelogout',auth_views.LogoutView.as_view(next_page='home'),name="servicelogout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_from.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
 
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('relogin',views.relogin),

    path('registerlogin',views.registerlogin,name="register"),
    path('profile',views.profile,name="profile"),
    #-------contact 
    path('contact',views.contact,name="contact"),
    #path('scenquire',views.scenquire),

    #-----roadside----
    path('roadside',views.roadside),
  
    #----redirect-------
    path('rhome',views.rhome),
    #--------service------
    path('detailing',views.detailing),
    path('painting',views.painting),
    path('acservice',views.acservice),
    path('custom',views. custom),
    path('insurance',views.insurance),
    #----booking-
    path('booking/<package>',views.book_appointment , name='book_appointment'),

    #-----------------------------------
    path('paper',views.show_item),
    
    



]
  

  
   

   

