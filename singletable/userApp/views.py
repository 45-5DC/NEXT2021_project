from django.shortcuts import render, redirect #, HttpResponse
from django.contrib.auth.models import User
from userApp.models import Profile
from django.contrib import auth

# 이메일 인증 관련
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token

# Create your views here.
def main(request):
    recipes = RecipePost.objects.all()
    purchases = PurchasePost.objects.all()

    return render(request, 'main.html', {'recipes': recipes, 'purchases': purchases})

def signup(request):
    if (request.method == 'POST'):
        found_user = User.objects.filter(username=request.POST['username'])
        if (len(found_user) > 0):
            error = '같은 아이디가 이미 존재합니다.'
            return render(request, 'signup.html', {
                'error': error})
        
        # if request.POST['password1'] == request.POST['password2']:
        new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password'],
        )
        new_user.is_active = False
        new_user.save()

        profile = Profile()
        profile.user = new_user
        profile.email = request.POST['email']
        profile.nickname = request.POST['nickname']
        profile.profile_img = request.FILES['profile_img']
        profile.intro = request.POST['intro']
        profile.save()

        current_site = get_current_site(request)
        message = render_to_string('email_activation.html', {
            'user': new_user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)).encode().decode(),
            'token': account_activation_token.make_token(user),
        })
        mail_title = "계정 활성화 확인 이메일"
        user_email = new_user.profile.email #request.POST['email']
        email = EmailMessage(mail_title, message, to=[user_email])
        email.send()
        # return HttpResponse(
        #     '<div style="font-size: 40px; width: 100%; height:100%; display:flex; text-align:center; '
        #     'justify-content: center; align-items: center;">'
        #     '입력하신 이메일<span>로 인증 링크가 전송되었습니다.</span>'
        #     '</div>'
        # )

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

def activate(request, uid64, token):
    uid = force_text(urlsafe_base64_decode(uid64))
    user = User.objects.get(pk=uid)

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect('main')
    else:
        # return HttpResponse('비정상적인 접근입니다.')
        return render(request, 'main.html', {'error': '계정 활성화 오류'})
    return
    
def portal_verify(request):

    return render(request, 'user/portal_verify.html')

def verification_code(request):

    return render(request, 'user/verification_code.html')

def new_password(request):

    return render(request, 'user/new_password.html')