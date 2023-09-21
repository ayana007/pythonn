from . import views
from django.urls import path
urlpatterns = [

    path('',views.home,name='home') ,


     # path('add/', views.addition, name='addition'),

    # path('subtraction/',views.subtraction,name='subtraction'),
    # path('div/',views.div,name='division')
 ]




# path('about/',views.about,name='about.html'),
#     path('contact/',views.contact,name='contact'),
#     path('detail/',views.detail,name='detail.html'),
#     path('Thanks/',views.Thanks,name='Thanks')