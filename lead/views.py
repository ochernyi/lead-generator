from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from lead.forms import LeadForm, SignUpForm, LoginForm
from lead.models import User


class Index(LoginRequiredMixin, generic.FormView):
    form_class = LeadForm
    template_name = "index.html"


class UserCreateView(generic.CreateView):
    model = User
    form_class = SignUpForm
    template_name = "user_form.html"
    success_url = reverse_lazy("lead:index")


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("lead:index")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "index.html")
