from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import FormView
from .models import Services, Team, Features
from .forms import ContactForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Services.objects.all().order_by("?").all()
        context['team'] = Team.objects.all()
        right = []
        left = []
        for i, feature in enumerate(Features.objects.all().order_by("?").all()):
            if i % 2 == 0:
                right.append(feature)
            else:
                left.append(feature)
        
        context['right_features'] = right
        context['left_features'] = left
        return context
    
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Email sent successfully')    
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'error ocurred')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
