from django.shortcuts import render
from .models import User
# Create your views here.
from django.http import HttpResponse

def homePageView(request):
	return render(request, 'index.html')
def aboutPageView(request):
	return render(request, 'about.html')
def servicePageView(request):
	return render(request, 'service-list.html')
def trainingPageView(request):
	return render(request, 'testimonials.html')
def contactPageView(request):
	return render(request, 'contact-us.html')
def infoPageView(request):
	return render(request, 'vat-info.html')
def rulesPageView(request):
	return render(request, 'vat-rules.html')
def lawPageView(request):
	return render(request, 'vat-law.html')

def completePageView(request):
	fname=request.POST["fname"]
	lname=request.POST["lname"]
	email=request.POST["email"]
	phone=request.POST["phone"]
	textarea=request.POST["textarea"]

	user=User(fname=fname,lname=lname,email=email,phone=phone,textarea=textarea)
	user.save()
	return render(request, 'contact-us.html')