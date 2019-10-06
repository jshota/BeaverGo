from django.shortcuts import render

# Create your views here.

def get_index(request):
	title = "BeaverGo"
	return render(request, 'index.html', {'title': title})

def get_signup(request):
	title = "SignUp Page"
	home = "BeaverGo"
	return render(request, 'signup.html', {'title': title, 'home': home})

def get_provider(request):
	title = "Provider Application"
	home = "BeaverGo"
	return render(request, 'provider.html', {'title': title, 'home': home})