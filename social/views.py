from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.views import View
from .models import Profile
from .forms import ProfileForm

# Create your views here.

@csrf_exempt
def home_view(request):
    context = {}
    return render(request, 'social/home.html', context)

@csrf_exempt
def login_view(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    query = 'SELECT * FROM social_profile WHERE "email" = "%s" AND "password" = "%s"' % (email, password)
    query_result = Profile.objects.raw(query)
    context = {}
    if query_result:
        context['query_result'] = query_result
        return render(request, 'social/login.html', context)
    else:
        return render(request, 'social/home.html', context)

@method_decorator(csrf_exempt, name='dispatch')
class ProfileView(View):
    def get(self, request):
        pk = request.GET.get('pk')
        profile = Profile.objects.get(pk=pk)
        return render(request, 'social/profile.html', {'profile': profile, 'request': request})

    def post(self, request):
        profile = Profile.objects.get(pk=request.POST.get('pk'))
        for key, value in request.POST.items():
            attr = getattr(profile, key, None)
            if attr:
                setattr(profile, key, value)
        profile.save()
        return HttpResponse("<h1>Done</h1>")


def search_view(request):
    search_word = request.GET.get('search')
    profiles = Profile.objects.filter(name=search_word)
    context = {
        'profiles': profiles
    }
    return render(request, 'social/search.html', context)
