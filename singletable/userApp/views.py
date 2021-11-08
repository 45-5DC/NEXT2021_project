from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from userApp.models import Profile
from django.contrib import auth

# Create your views here.
def signup(request):
    if (request.method == 'POST'):
        found_user = User.objects.filter(username=request.POST['username'])
        if (len(found_user) > 0):
            error = '같은 아이디가 이미 존재합니다.'
            return render(request, 'signup.html', {
                'error': error})
        
        # if request.POST['password1'] == request.POST['password2']:
        new_user = User.objects.create(
            username = request.POST['username'],
            password = request.POST['password'],
        )

        profile = Profile()
        profile.user = new_user
        profile.email = request.POST['email']
        profile.nickname = request.POST['nickname']
        profile.profile_img = request.FILES['profile_img']
        profile.intro = request.POST['intro']
        profile.save()

        auth.login(request, new_user)
        return redirect('main')

    return render(request, 'signup.html')

def login(request):
    if (request.method == 'POST'):
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password'],
        )

        if (found_user is None):
            error = '아이디 또는 비밀번호가 틀렸습니다.'
            return render(request, 'login.html', {
                'error': error
                })
            auth.login(request, found_user)
            return redirect('main')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)

    return redirect('main')
    
def portal_verify(request):

    return render(request, 'user/portal_verify.html')

def verification_code(request):

    return render(request, 'user/verification_code.html')

def new_password(request):

    return render(request, 'user/new_password.html')