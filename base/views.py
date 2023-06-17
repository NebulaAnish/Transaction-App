# Utility imports
from django.core.exceptions import PermissionDenied
from typing import Any, Dict
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

# CRUD imports
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from .models import Transaction
# user related imports
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Login Logout views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
# Account Registration and Profile forms
from .forms import NewUserForm
from .forms import ProfileForm
# User
from django.contrib.auth.models import User
# http
from django.http import Http404
# Views Start here.


class CustomRegisterView(CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy('login')
    template_name = 'base/register.html'


@login_required
def profile(request):
    return render(request, 'base/profile.html')


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("listview")


class CustomLogoutView(LogoutView):
    template_name = 'base/logout.html'
    next_page = 'login'


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('listview')
    template_name = 'base/profileEdit.html'
    context_object_name = 'user'


class CustomListView(LoginRequiredMixin, ListView):
    model = Transaction
    context_object_name = 'transactions'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transactions'] = context['transactions'].filter(
            user=self.request.user)
        context['count'] = context['transactions'].count()
        return context


class CustomCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    fields = ['title', 'amount', 'category']
    template_name = 'base/transaction_create.html'
    success_url = reverse_lazy('listview')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CustomDetailView(LoginRequiredMixin, DetailView):
    model = Transaction
    context_object_name = 'transaction'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.user != request.user:
            return self.handle_permission_denied()
        return super().dispatch(request, *args, **kwargs)

    def handle_permission_denied(self):
        redirect_url = reverse_lazy('forbidden')
        return HttpResponseRedirect(redirect_url)


class CustomUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction
    fields = ['title', 'amount', 'category']
    template_name = 'base/transaction_update.html'
    context_object_name = 'transaction'
    success_url = reverse_lazy('listview')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.user != request.user:
            return self.handle_permission_denied()
        return super().dispatch(request, *args, **kwargs)

    def handle_permission_denied(self):
        redirect_url = reverse_lazy('forbidden')
        return HttpResponseRedirect(redirect_url)


class CustomDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    template_name = 'base/delete_confirm.html'
    success_url = reverse_lazy('listview')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.user != request.user:
            return self.handle_permission_denied()
        return super().dispatch(request, *args, **kwargs)

    def handle_permission_denied(self):
        redirect_url = reverse_lazy('forbidden')
        return HttpResponseRedirect(redirect_url)


class ForbiddenView(TemplateView):
    template_name = 'base/forbidden.html'
