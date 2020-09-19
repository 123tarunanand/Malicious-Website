from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.core import serializers
from social.models import Profile


# Create your views here.

class SecureHomeView(View):
    def get(self,request):
        try:
            profile = Profile.objects.get(pk=request.session['user_id'])
            return render(request, 'secure/home_profile.html',{'profile':profile})
        except:
            return redirect('secure_login_view')

    def post(self, request):
        profile = Profile.objects.get(pk=request.session['user_id'])
        for key, value in request.POST.items():
            attr = getattr(profile, key, None)
            if attr:
                setattr(profile, key, value)
        profile.save()
        return HttpResponse("<h1>Done</h1>")

@csrf_exempt
def secure_login_view(request):
    try:
        profile = Profile.objects.get(pk=request.session['user_id'])
        return render(request, 'secure/home_profile.html',{'profile':profile})
    except:
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            profile = Profile.objects.get(email=email, password=password)
            request.session['user_id'] = profile.pk
            return redirect('secure_home_view')
        except:
            return render(request, 'secure/home.html')

@csrf_exempt
def secure_logout_view(request):
    del request.session['user_id']
    return redirect('secure_login_view')


class SecureProfileView(View):
    def get(self, request, pk):
        profile = Profile.objects.get(pk=pk)
        return render(request, 'secure/profile.html', {'profile': profile, 'request': request})

    def post(self, request, pk):
        post_pk = int(request.POST.get('pk'))
        if post_pk != request.session['user_id']:
            return HttpResponse("<h1>Access Denied</h1>")
        profile = Profile.objects.get(pk=request.POST.get('pk'))
        for key, value in request.POST.items():
            attr = getattr(profile, key, None)
            if attr:
                setattr(profile, key, value)
        profile.save()
        return HttpResponse("<h1>Done</h1>")


class SecureProfileInfoView(View):
    def get(self, request):
        email = request.GET.get('email')
        password = request.GET.get('password')
        try:
            profile = Profile.objects.get(email=email, password=password)
            ser = serializers.serialize('json', query_result)
            return JsonResponse(ser, safe=False)
        except:
            return JsonResponse([], safe=False)


@csrf_exempt
def secure_search_view(request):
    search_word = request.GET.get('search')
    profiles = Profile.objects.filter(name=search_word)
    context = {
        'profiles': profiles
    }
    return render(request, 'secure/search.html', context)
