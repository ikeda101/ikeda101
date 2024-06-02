from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import Profile
from .forms import ProfileUpdateForm
from utils.access_restrictions import OwnProfileOnly

class ProfileUpdateView(OwnProfileOnly, UpdateView):
    template_name = "accounts/profile-form.html"
    model = Profile
    form_class=ProfileUpdateForm
    success_url = reverse_lazy("nippo-list")