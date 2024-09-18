from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/register.html', {'form': form})

from django.contrib.auth import login as auth_login
from django.shortcuts import redirect, render
from .models import Profile

def login(request):
    if request.method == 'POST':
        # Handle login logic
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if Profile.objects.filter(user=user).exists():
                auth_login(request, user)
                return redirect('homepage')
            else:
                return redirect('create_profile')
        else:
            # Invalid login
            pass
    return render(request, 'account/login.html')

from django.shortcuts import render
from .models import Profile

def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    donations = BloodDonationRequest.objects.filter(user=request.user)
    return render(request, 'account/profile.html', {'profile': profile, 'donations': donations})

from django.views.generic.edit import UpdateView
from django.utils import timezone
from datetime import timedelta

class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['first_name', 'last_name', 'weight', 'height', 'region', 'province', 'municipality', 'availability']

    def form_valid(self, form):
        if form.instance.availability:
            days_since_last_donation = (timezone.now().date() - form.instance.last_donation_date).days
            if days_since_last_donation < 56:
                form.add_error('availability', f'You must wait {56 - days_since_last_donation} days before being available.')
                return self.form_invalid(form)
        return super().form_valid(form)
