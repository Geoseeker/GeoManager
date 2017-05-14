from django.shortcuts import render
from django.views import View
from GeoRiddles.models import Mystery
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from GeoRiddles.forms import AddMysteryForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, get_user_model
from django.http import HttpResponseRedirect

class BaseView(View):
    def get(self, request):
        return render(request, 'base.html')

class MysteryView(View):
    def get(self, request):
        mystery = Mystery.objects.all()
        ctx = {'mystery' : mystery}
        return render(request, 'mystery.html', ctx)

class DetailMystery(View):
    def get(self, request, id):
        riddle = Mystery.objects.get(id=id)
        ctx = {'detail' : riddle}
        return render(request, 'mystery_detail.html', ctx)

class AddMystery(CreateView):
    model = Mystery
    fields = '__all__'
    success_url = reverse_lazy('mystery')

class AddMystery(View):
    def get(self,request):
        form = AddMysteryForm(initial={'added_by': request.user})
        ctx = {'form' : form}
        return render(request, 'add_mystery.html', ctx)
    def post(self, request):
        form = AddMysteryForm(data=request.POST)
        ctx = {'form' : form}
        if form.is_valid():
            name = form.cleaned_data['name']
            gc_code = form.cleaned_data['gc_code']
            description = form.cleaned_data['description']
            location = form.cleaned_data['location']
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            added_by = form.cleaned_data['added_by']
            Mystery.objects.create(
                name = name,
                gc_code = gc_code,
                description = description,
                location = location,
                latitude = latitude,
                longitude = longitude,
                added_by = request.user)
            return HttpResponseRedirect('mystery')
        return render(request, 'add_mystery.html', ctx)
