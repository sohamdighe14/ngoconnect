from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from .models import Event
from .forms import EventCreateForm
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


class EventListView(LoginRequiredMixin,ListView):
    # queryset = DonorProfile.objects.all()
    template_name = 'events/event_list.html'
    def get_queryset(self):
        queryset = Event.objects.filter(owner=self.request.user)
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


class EventDetailView(LoginRequiredMixin,DetailView):
    template_name= 'events/event_details.html'
    def get_queryset(self):
        queryset = Event.objects.filter(owner=self.request.user)
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
class EventCreateView(LoginRequiredMixin,CreateView):
    form_class=EventCreateForm
    template_name='events/form.html'
    #success_url='/details/'

    def form_valid(self,form):
        instance=form.save(commit=False)
        instance.owner=self.request.user
        return super(EventCreateView,self).form_valid(form)

class EventUpdateView(LoginRequiredMixin,UpdateView):
    model=Event
    form_class=EventCreateForm
    template_name='events/form.html'

    def get_context_data(self, *args, **kwargs):
        context = super(EventUpdateView, self).get_context_data(*args, **kwargs)
        #context['title'] = 'Add Restaurant'
        return context

    def get_queryset(self):
        queryset = Event.objects.filter(owner=self.request.user)
        return queryset
