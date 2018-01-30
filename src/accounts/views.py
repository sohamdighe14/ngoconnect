from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from .models import DonorProfile
from .forms import DonorProfileCreateForm
# Create your views here.

# def donor_createview(request):
#     form=DonorProfileCreateForm()
#     error=None
#     if request.method=='POST':
#         form=DonorProfileCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # obj=DonorProfile.objects.create(
#             #         name            =   form.cleaned_data.get('name'),
#             #         occupation      =   form.cleaned_data.get('occupation'),
#             #         location        =   form.cleaned_data.get('location'),
#             #         date_of_birth   =   form.cleaned_data.get('date_of_birth'),
#             #         address         =   form.cleaned_data.get('address')
#             # )
#         return HttpResponseRedirect('/details/') 
#         if form.errors:
#             print(form.errors)
#             error=form.errors 
#     template_name='accounts/form.html'
#     context={
#         'form':form,
#         'errors':error,
#     }
#     return render(request,template_name,context)
        
class HomeView(LoginRequiredMixin,TemplateView):
    template_name = "home.html"


class DonorListView(LoginRequiredMixin,ListView):
    # queryset = DonorProfile.objects.all()
    template_name = 'accounts/donor_list.html'
    def get_queryset(self):
        queryset = DonorProfile.objects.filter(owner=self.request.user)
        return queryset
    # def get_queryset(self):
    #     slug=self.kwargs.get("slug")
    #     if slug:
    #         queryset=DonorProfile.objects.filter(Q(name__iexact=slug)|Q(name__icontains=slug))
    #         #hasattr(queryset, name)
    #             # Q(occupation__iexact='singer')|
    #             # Q(address__iexact='kanto')
    #             # )
    #     else:
            
     #   return queryset


class DonorDetailView(LoginRequiredMixin,DetailView):
    template_name= 'accounts/donor_details.html'
    def get_queryset(self):
        queryset = DonorProfile.objects.filter(owner=self.request.user)
        return queryset
        
    # def get_context_data(self, *args, **kwargs):
    #     print(self.kwargs)
    #     context = super(DonorDetailView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context
#   if u do not pk or slug but someting like rest_id 
#     def get_object(self, *args, **kwargs):
#         rest_id = self.kwargs.get('rest_id')
#         obj=get_object_or_404(DonorList,id=rest_id)
#         return obj
class DonorCreateView(LoginRequiredMixin,CreateView):
    form_class=DonorProfileCreateForm
    template_name='accounts/form.html'
    #success_url='/details/'

    def form_valid(self,form):
        instance=form.save(commit=False)
        instance.owner=self.request.user
        return super(DonorCreateView,self).form_valid(form)

class DonorUpdateView(LoginRequiredMixin,UpdateView):
    model=DonorProfile
    form_class=DonorProfileCreateForm
    template_name='accounts/form.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DonorUpdateView, self).get_context_data(*args, **kwargs)
        #context['title'] = 'Add Restaurant'
        return context