from django.shortcuts import render

# Create your views here.


def principal(request):
    return render(request, 'booking_page.html')