from django.shortcuts import render

# Create your views here.

def get_index(request):
	title = "BeaverGo~"
	return render(request, 'index.html', {'title': title})