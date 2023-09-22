from django.urls import path
from django.contrib.auth import views as auth_views
from custom_accounts import views
from custom_accounts.forms import MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    path('login/', views.signin, name='login'),
    path('login_request/', views.User_login, name='login_request'),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.signup, name='register'),
    path('register_request/', views.User_register, name='register_request'),

    path('profile/<int:pk>/', views.userProfile, name='user-profile'),
    path('change_pass_page/', views.password_change_page, name='change_pass_page'),
    path('change_pass_request/', views.password_change_request, name='change_pass_request'),

    #Forget Password
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='base/password_reset_form.html', form_class=MyPasswordResetForm), name='password_reset'),
    
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='base/password_reset_done.html'), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='base/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='base/password_reset_complete.html'), name='password_reset_complete'),
]

