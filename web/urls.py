from django.urls import path
from .views import HomePageView, AboutPageView, HelpPageView

app_name = 'web'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(template_name='web/about.html'), name='about'),
    path('help/', HelpPageView.as_view(template_name='web/help.html'), name='help'),
]