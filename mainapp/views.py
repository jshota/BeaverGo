from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os

# Create your views here.

def get_index(request):
	title = "BeaverGo"
	return render(request, 'index.html', {'title': title})

def get_provider(request):
	title = "Provider Signup Page"
	home = "BeaverGo"
	return render(request, 'provider.html', {'title': title, 'home': home})

def get_passenger(request):
	title = "Passenger Signup Page"
	home = "BeaverGo"
	return render(request, 'passenger.html', {'title': title, 'home': home})

def get_driver(request):
	title = "Driver Signup Page"
	home = "BeaverGo"
	return render(request, 'driver.html', {'title': title, 'home': home})

@csrf_exempt
def github_webhook(request):
        if request.method == 'POST':
            os.chdir('/home/ubuntu/BeaverGo')
            os.system("git pull")
            os.system("git add .")
            os.system("git commit -m 'Server: update'")
            os.system("git push origin master")
            return HttpResponse('Done')
        return HttpResponse('Use POST please')
