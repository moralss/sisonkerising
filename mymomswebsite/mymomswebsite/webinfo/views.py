from django.shortcuts import render

def index(request):
    return render(request, 'webinfo/home.html')

def Contact(request):
    return render(request, 'webinfo/Contact.html')

	
	
def About(request):
    return render(request, 'webinfo/About.html')
