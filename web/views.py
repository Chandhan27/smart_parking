from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import HelpForm

app_name = 'web'

class HomePageView(TemplateView):
    template_name = 'web/home.html'
    extra_context = {}
 
class AboutPageView(TemplateView):
    template_name = 'web/about.html'
    extra_context = {}

class HelpPageView(TemplateView):
    template_name = 'web/help.html'
    extra_context = {}

def help_center(request):
    if request.method == 'POST':
        form = HelpForm(request.POST)
        if form.is_valid():
            # Here you can process the form data (save to DB or send email)
            print("Form Submitted:", form.cleaned_data)
            return render(request, 'help_center.html', {'form': HelpForm(), 'success': True})
    else:
        form = HelpForm()
    return render(request, 'help_center.html', {'form': form})

