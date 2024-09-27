from django.urls import path
from . import views
app_name='info'
urlpatterns = [
    path('contact/',views.contact,name='contact'),
    path('',views.home,name='home'),
    path("confirm-contact/",views.confirm_contact,name='confirm_contact'),
]
