from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def upload(request):
    return render(request, 'upload.html')
def documentation(request):
    return render(request, 'documentation.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def features(request):
    return render(request, 'features.html')