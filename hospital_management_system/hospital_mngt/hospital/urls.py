from django.urls import path
from .views import about, home, contact, Login, Logout_admin

urlpatterns = [
    path('', home,name='home'),
    path('about/', about,name='about'),
    path('contact/', contact,name='contact'),
    path('admin_login/', Login,name='login'),
    path('logout/', Logout_admin,name='logout_admin'),    
]