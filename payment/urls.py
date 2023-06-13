
from django.urls import path
from payment import views
urlpatterns = [
    
    path('', views.index, name='index'),
    path('thanks/', views.thanks, name='thanks'),
    path('checkout/', views.checkout, name='checkout'),
    path('stripe_webhook/', views.stripe_webhook, name='stripe_webhook')
]
