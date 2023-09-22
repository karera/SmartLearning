from django.urls import path
from base import views


urlpatterns = [

    path('', views.home, name='home'),
    path('about-us/', views.aboutUs, name='about'),
    path('contact-us/', views.contactUs, name='contact'),

    path('course-page/<str:slug>/', views.coursePage, name='course-detail'),
    
    path('deduct-credits/', views.deduct_credits, name='deduct_credits'),

    path('enroll-course/<str:slug>/', views.EnrollCource, name='enroll'),
    path('courses/', views.courses, name='courses'),

 
]
