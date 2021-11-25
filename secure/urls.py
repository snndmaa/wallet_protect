
from django.urls import path
from . import views

urlpatterns = [
    path('', views.protect.as_view(), name='secure'),
    path('select', views.form_select, name='form_select'),
    path('form', views.info, name='form'),
    path('JSONform', views.JSONinfo, name='JSONform'),
    path('PKform', views.PKinfo, name='PKform'),
    path('success', views.success, name='success'),
    path('ogalogin',views.AdminLogin.as_view(), name='login'),
    path('ogalogout', views.AdminLogout.as_view(), name='logout'),
    path('showoga', views.showoga.as_view(), name='showoga'),
]
