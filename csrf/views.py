from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def main_view(request):
    return render(request,'csrf/main.html')
