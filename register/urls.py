from django.urls import path
from . import views

urlpatterns = [
    path('',views.register,name='register'),
    path('login',views.login,name='login'),
    path('add',views.add1,name='add1'),
    path('log',views.log1,name='log1'),
    path('create',views.create1,name='create1'),
    path('manage',views.manage1,name='manage1'),
    path('approval',views.approval1,name='approval1'),
    path('new',views.vehicle1,name='vehicle1'),
    path('gatepass',views.gatepass1,name='gatepass1'),
    path('approver_reg',views.approver_reg1,name='approver_reg1'),
    path('app_log',views.app_log1,name='app_log1'),
    path('app_login',views.app_login1,name='app_login1'),
    path('approval_log',views.approval_log1,name='approval_log1'),
]

