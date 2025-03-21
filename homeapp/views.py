from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Add logic to process the data (e.g., save to the database, send an email)
        print(f"Received message from {name} ({email}): {message}")
        return HttpResponse("Thank you for contacting us!")

    return render(request,'contact.html')  # Ensure this matches your template name
