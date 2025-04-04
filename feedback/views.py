from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import FeedbackForm
from django.contrib import messages

class FeedbackCreateView(CreateView):
    template_name = 'feedback_form.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        messages.success(self.request, 'Thank you for your feedback!')
        return super().form_valid(form)