from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from .models import Profile

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

def profile_view(request, profile_id):
    profile = Profile.objects.get(pk=profile_id)
    context = {
        'profile': profile
    }
    return render(request, 'social/profile.html', context)


def search_view(request):
    search_word = request.GET.get('search')
    profiles = Profile.objects.filter(name=search_word)
    context = {
        'profiles': profiles
    }
    return render(request, 'social/search.html', context)
