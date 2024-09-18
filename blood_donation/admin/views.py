from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from blood.models import BloodDonationRequest
from account.models import User

@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    users = User.objects.all()
    donations = BloodDonationRequest.objects.all()
    return render(request, 'admin_app/dashboard.html', {'users': users, 'donations': donations})
