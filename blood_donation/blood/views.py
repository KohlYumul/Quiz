from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import BloodDonationRequest

class BloodDonationCreateView(CreateView):
    model = BloodDonationRequest
    fields = ['request_type', 'blood_type', 'region', 'province', 'municipality', 'description']

    def form_valid(self, form):
        if form.instance.request_type == 'donating':
            form.instance.region = self.request.user.profile.region
            form.instance.province = self.request.user.profile.province
            form.instance.municipality = self.request.user.profile.municipality
            form.instance.blood_type = self.request.user.profile.blood_type
        return super().form_valid(form)

class BloodDonationUpdateView(UpdateView):
    model = BloodDonationRequest
    fields = ['description']

class BloodDonationDeleteView(DeleteView):
    model = BloodDonationRequest
    success_url = '/blood/list/'

class BloodDonationListView(ListView):
    model = BloodDonationRequest
    template_name = 'blood/donation_list.html'

class BloodDonationDetailView(DetailView):
    model = BloodDonationRequest
    template_name = 'blood/donation_detail.html'
