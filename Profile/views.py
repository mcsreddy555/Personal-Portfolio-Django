from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Contact
# Create your views here.


# Home/Index View
def index(request):
     return render(request, 'mypf/home.html')


#Portfolio View
def portfolio(request):
    return render(request, 'mypf/portfolio.html')


# Contact View
def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        form = Contact(email=email, subject=subject, message=message)
        # Saving Form data to Database
        form.save()

        return render(request, 'mypf/contact.html')
    else:
        return render(request, 'mypf/contact.html')
