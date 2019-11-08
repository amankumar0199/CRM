from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
path('ActivityReport',views.ActivityReport.as_view(),name="ActivityReport"),
path('working/',views.WorkingDetail,name = 'working'),
path('',views.home, name='home'),
path('forms/',views.ActivityF,name="ActivityF"),
path('workinginfo/',views.EnterWorking.as_view(), name='add_working'),
]
