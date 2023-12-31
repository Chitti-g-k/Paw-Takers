from django.shortcuts import render, redirect, get_object_or_404,HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import ListView,View
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserProfileForm
from django.forms import formset_factory
from .forms import UserProfileForm, ServiceDescriptionForm



def display(request):
     profiles = UserProfile.objects.all()
     
     selected_city = request.GET.get('city')
     if selected_city:
          profiles = profiles.filter(city=selected_city)
     
     cities = UserProfile.objects.values_list('city', flat=True).distinct()
     
     context = {
          'profiles': profiles,
          'cities': cities,
          'selected_city': selected_city,
     }
     
     return render(request, 'home.html', context)





def index(request):
     user_count = UserProfile.objects.count()
     city_count = UserProfile.objects.values('city').distinct().count()
     state_count = UserProfile.objects.values('state').distinct().count()
     
     context = {
          'user_count': user_count,
          'city_count': city_count,
          'state_count': state_count
     }
     
     return render(request,'index.html',context)


class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
          profile = UserProfile.objects.get(pk=pk)
          user = profile.user
          service_descriptions = profile.services_description.all()
          
          context = {
               'user': user,
               'profile': profile,
               'service_descriptions': service_descriptions,
          }

          return render(request, 'profilepage.html', context)

     

class UserProfileForm(forms.ModelForm):
     class Meta:
          model = UserProfile
          exclude = ['id']
          


class Data(View):
     def get(self, request, *args, **kwargs):
          form = UserProfileForm()
          context = {
               'form': form,
          }
          return render(request, 'form.html', context)

     def post(self, request, *args, **kwargs):
          form = UserProfileForm(request.POST, request.FILES)
          
          if form.is_valid():
               new_profile = form.save(commit=False)
               new_profile.user = request.user
               new_profile.save()
               
               services = form.cleaned_data.get('services_description')
               for service in services:
                    ServiceDescription.objects.create(user_profile=new_profile, service=service)
               
               return redirect('/display')
          
          return render(request, 'form.html', {'form': form})

class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
     model = UserProfile
     
     fields = ['name', 'image', 'phone_number', 'backup_phonenumber', 'description', 'services_description', 'form_number', 'first_line', 'second_line', 'city', 'state', 'postal_code']
     template_name = 'profile_edit.html'
     
     
          
     def get_success_url(self):
          pk = self.kwargs['pk']
          return HttpResponseRedirect(reverse_lazy('/profile', kwargs={'pk': pk}))
          
     def test_func(self):
          profile = self.get_object()
          return self.request.user == profile.user
     
