from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def booking(request):
    return render(request, 'booking.html')

@login_required(login_url='login')
def team(request):
    return render(request, 'team.html')

@login_required(login_url='login')
def testimonial(request):
    return render(request, 'testimonial.html')
