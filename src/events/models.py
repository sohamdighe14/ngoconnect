from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
import datetime

from .utils import unique_slug_generator
from .validators import validate_category

# Create your models here.

User = settings.AUTH_USER_MODEL


class EventQuerySet(models.query.QuerySet):
    def search(self,query):
        if query: 
            query=query.strip()   
            return self.filter(
                Q(event_name__icontains=query)|
                Q(location__icontains=query)|
                Q(address__icontains=query)
                ).distinct()
        else:
            return self


class EventManager(models.Manager):
    def get_queryset(self):
        return EventQuerySet(self.model,using=self._db)


    def search(self,query):
        return self.get_queryset().search(query)


class Event(models.Model):
    owner           =   models.ForeignKey(User)
    event_name      =   models.CharField(max_length=120)
    description     =   models.TextField(blank=True, null=True)
    location        =   models.CharField(max_length=120)
    date_of_event   =   models.DateField(default=datetime.date.today)
    address         =   models.CharField(max_length=256,blank=True, null=True,validators=[validate_category])
    slug            =   models.SlugField(blank=True, null=True)

    objects=EventManager()      #adding search func
    
    def __str__(self):
        return self.event_name

    def get_absolute_url(self): #get_absolute_url
       return reverse('events:Details', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.event_name

def event_pre_save_reciever(sender,instance,*args,**kwargs):
    instance.event_name=instance.event_name.capitalize()
    instance.location=instance.location.capitalize()
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

# def dp_post_save_reciever(sender,instance,created,*args,**kwargs):
#     print('saved')
#     print(instance.location)
#     if not instance.slug:
#         instance.slug=unique_slug_generator(instance)
#         instance.save()

pre_save.connect(event_pre_save_reciever,sender=Event)

# post_save.connect(dp_post_save_reciever,sender=DonorProfile)
