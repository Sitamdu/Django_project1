from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    views = {}
    views['services'] = Service.objects.all()
    views['feedbacks'] = Feedback.objects.all()
    if request.method == 'POST':
        email = request.POST['EMAIL']
        data = Subscribe.objects.create(
            email = email
        )
        data.save()
        return render(request, 'index.html')

    return render(request, 'index.html',views)
def about(request):
    return render(request, 'about.html')
def contact(request):
    views = {}
    views['infos'] = Information.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        data.save()
        views['mess'] = 'The message is Submitted!'
        return render(request, 'contact.html',views)

    return render(request, 'contact.html',views)
def portfolio(request):
    return render(request, 'portfolio.html')
def services(request):
    return render(request, 'services.html')
def price(request):
    return render(request, 'price.html')
def blog_home(request):
    return render(request, 'blog-home.html')
def blog_single(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Blogsingle.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        data.save()
        messages = {'mess':'The message is submitted!'}
        return render(request, 'blog-single.html',messages)

    return render(request, 'blog-single.html')
def elements(request):
    views = {}
    views['countries'] = Element.objects.all()

    return render(request, 'elements.html',views)



