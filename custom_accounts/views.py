from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages , auth
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404,JsonResponse,HttpResponseBadRequest
from django.contrib.auth import get_user_model, authenticate, login, logout
from custom_accounts.models import  User
from base.models import UserProfile
from custom_accounts.forms import UserForm, MyUserCreationForm, EditProfileForm, ChangePasswordForm
from django.utils import timezone
import os
from social_django.utils import psa

from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

#login page
def signin(request):
    return render(request, 'base/signin.html')

#User login function
@api_view(['POST'])
def User_login(request):
    context={}
    user=None
    if request.method=='POST':
        
        email = request.data['email']
        password = request.data['password']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            context['message'] = 'User does not exist'
            context['status'] = 'Error'
            context['code']=status.HTTP_401_UNAUTHORIZED
            return JsonResponse(context, status = 200)

        if user.social_auth.exists() and not user.has_usable_password():
            context['message'] = 'Account created by social-auth. <br/>Please login first through social-auth then change your password via your profile page at least 1 time.<br/> So you will be able to login via custom login ( email + password )'
            context['status'] = 'Error'
            context['code']=status.HTTP_401_UNAUTHORIZED
            return JsonResponse(context, status = 200)
        
        user= auth.authenticate(email=email,password=password)
        
        if user and user.has_usable_password():
            auth.login(request, user)
            context['message'] = 'connected'
            context['status'] = 'Success'
            context['code']=status.HTTP_200_OK
            return JsonResponse(context, status = 200)
        elif not user:
            user_account = User.objects.filter(email = email,is_active=False)
            if user_account:
                context['message'] = "You haven't yet activated your account to access. Check your mail please"
                context['status'] = 'Error'
                context['code']=status.HTTP_401_UNAUTHORIZED    
                return JsonResponse(context, status = 200)
            elif not user_account:
                context['message'] = 'Credentials not valid.<br/>Email or password incorrect, please try again'
                context['status'] = 'Error'
                context['code']=status.HTTP_401_UNAUTHORIZED
                return JsonResponse(context, status = 200)
        else :
            context['message'] = 'error server'
            context['status'] = 'Error'
            context['code']=status.HTTP_401_UNAUTHORIZED           
            return JsonResponse(context, status = 200)
    
    return JsonResponse({}, status = 200)

#register page
def signup(request):
    form = MyUserCreationForm()
    context = {'form': form}
    
    return render(request, 'base/signup.html', context)

@api_view(['POST'])
def User_register(request):
    context={}

    if request.method=='POST':

        form = MyUserCreationForm(request.data)
        username = request.data['username']
        email = request.data['email']
        password = request.data['password1']
        confirm_password = request.data['password2']

        user_account = User.objects.all().filter(email = email)

        if user_account:
            context['message'] = 'An user already used this email'
            context['status'] = 'Error'
            context['code']=status.HTTP_401_UNAUTHORIZED           
            return JsonResponse(context, status = 200)

        elif password == confirm_password:     
            if not user_account:
                
                if form.is_valid():
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    user= auth.authenticate(email=email,password=password)
                    auth.login(request, user)
                    context['message'] = "Thank you for joining us ! Enjoy"
                    context['status'] = 'Success'
                    context['code']=status.HTTP_200_OK
                    return JsonResponse(context, status = 200)
                else:
                    context['message'] = """
                    The form is not valid.<br/>
                    Verify if:<br/>
                    1-- your email is correct (example@email.com).<br/>
                    2-- your password has at least 8 characters 
                    and content at least 1 uppercase letter, 1 special character, and alphanumeric characters.<br/>
                    3-- your username is not too similar to your email.<br/>
                    """
                    context['status'] = 'Error'
                    context['code']=status.HTTP_401_UNAUTHORIZED           
                    return JsonResponse(context, status = 200)

            else:
                context['message'] = 'Credentials not valid'
                context['status'] = 'Error'
                context['code']=status.HTTP_401_UNAUTHORIZED           
                return JsonResponse(context, status = 200)
        else:
            context['message'] = 'Password and confirm password not same'
            context['status'] = 'Error'
            context['code']=status.HTTP_401_UNAUTHORIZED
            return JsonResponse(context, status = 200)
    return JsonResponse({}, status = 200)

#Logout
def logoutUser(request):
    logout(request)
    return redirect('home')


@login_required
def password_change_page(request):
    context={}
    user = request.user
    form = ChangePasswordForm(user)
    return render(request, 'base/change_password.html', {'form': form})

@login_required
@api_view(['POST'])
def password_change_request(request):
    context={}
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            context['message'] = "You have successfully set your password. <br/> Your account will be disconnected. <br/> Use your new password to login"
            context['status'] = 'Success'
            context['code']=status.HTTP_200_OK
            return JsonResponse(context, status = 200)
        else:
            context['message'] = """
            The form is not valid.<br/>
            Verify if:<br/>
            your password has at least 8 characters 
            and content at least 1 uppercase letter, 1 special character, and alphanumeric characters.<br/>
            """
            context['user'] = str(user.id)
            context['status'] = 'Error'
            context['code']=status.HTTP_401_UNAUTHORIZED
            return JsonResponse(context, status = 200)
    return JsonResponse({}, status = 200)

@login_required
def userProfile(request, pk):
    if request.user.is_authenticated and request.user.pk == pk:
        user = request.user
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        enrolled_courses = user_profile.course.all()
        remaining_free_credits = user_profile.free_credits
        credit_balance = user_profile.credits

        if request.method == 'POST':
            form = EditProfileForm(request.POST, request.FILES, instance=request.user)
            form2 = ChangePasswordForm(user, request.POST)

            if form2.is_valid():
                form2.save()
                user_pk = request.user.pk
                messages.success(request, "You have successfully set your password.")
                return redirect(reverse('user-profile', args=[user_pk]))
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

            if form.is_valid():
                form.save()
                user_pk = request.user.pk
                messages.success(request, "You have successfully updated profile.")
                return redirect(reverse('user-profile', args=[user_pk]))

            
        else:
            form = EditProfileForm(instance=request.user)
            form2 = ChangePasswordForm(user)

        context = {
            'user_profile': user_profile,
            'enrolled_courses': enrolled_courses,
            'remaining_free_credits': remaining_free_credits,
            'credit_balance': credit_balance,
            'form': form,
            'form2': form2,
        }
        return render(request, 'base/profile.html', context)
    else:
        return redirect('login')


# @login_required
def custom_google_login(request):
    user = request.user
    if user.social_auth.filter(provider='google').exists():
        messages.error(request, 'Cannot log in with Google for users who already used Google login.')
        return redirect('login')
    if User.objects.filter(email=user.email).exists():
        messages.error(request, 'Email is already registered. Please log in using the regular login form.')
        return redirect('login')

    # Social login logic for Google

# @login_required
def custom_twitter_login(request):
    user = request.user
    if user.social_auth.filter(provider='twitter').exists():
        messages.error(request, 'Cannot log in with Twitter for users who already used Twitter login.')
        return redirect('login')
    if User.objects.filter(email=user.email).exists():
        messages.error(request, 'Email is already registered. Please log in using the regular login form.')
        return redirect('login')

    # Social login logic for Twitter

@psa('social:complete')
def social_auth_complete(request, backend, *args, **kwargs):
    try:
        user = kwargs['user']
        social_user = user.social_auth.get(provider=backend)
    except User.DoesNotExist:
        return HttpResponseBadRequest('User not found')
    except SocialAuth.DoesNotExist:
        return HttpResponseBadRequest('Social account not found')

    if User.objects.filter(email=user.email).exists():
        messages.error(request, 'Email is already registered. Please log in using the regular login form.')
        return redirect('login')

    if social_user:
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return redirect('home')
    else:
        return HttpResponseBadRequest('Social account not linked')




