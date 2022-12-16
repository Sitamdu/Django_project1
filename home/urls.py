from .views import *
from django.urls import path


urlpatterns = [
    path('', home, name = 'home'),
    path('about', about, name = 'about'),
    path('contact', contact, name = 'contact'),
    path('portfolio', portfolio, name = 'portfolio'),
    path('services', services, name = 'services'),
    path('price', price, name = 'price'),
    path('blog_home', blog_home, name = 'blog_home'),
    path('blog_single', blog_single, name = 'blog_single'),
    path('elements', elements, name = 'elements'),

]