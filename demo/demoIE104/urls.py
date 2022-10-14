from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Uudiem/',views.index2,name='index2'),
    path('SoSanh/',views.index3,name='index3'),
    path('GiaiQuyet/',views.index4,name='index4'),
    path('LiDo/',views.index5,name='index5'),
    path('QuyTrinh/',views.index6,name='index6'),
]