from django.views.generic import TemplateView

# Create your views here.

class home(TemplateView):
    template_name = 'index.html'

class feature(TemplateView):
    template_name = 'content/cryptocurrency/features.html'

class transact(TemplateView):
    template_name = 'content/cryptocurrency/faq.html'