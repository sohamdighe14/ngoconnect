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

class DonorProfile(models.Model):
    owner           =   models.ForeignKey(User)
    name            =   models.CharField(max_length=120)
    occupation      =   models.CharField(max_length=120)
    location        =   models.CharField(max_length=120)
    date_of_birth   =   models.DateField(default=datetime.date.today)
    address         =   models.CharField(max_length=256,blank=True, null=True,validators=[validate_category])
    slug            =   models.SlugField(blank=True, null=True)
    #objects = DonorProfileManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self): #get_absolute_url
       return reverse('accounts:Details', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.name


def dp_pre_save_reciever(sender,instance,*args,**kwargs):
    instance.address=instance.address.capitalize()
    instance.occupation=instance.occupation.capitalize()
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

# def dp_post_save_reciever(sender,instance,created,*args,**kwargs):
#     print('saved')
#     print(instance.location)
#     if not instance.slug:
#         instance.slug=unique_slug_generator(instance)
#         instance.save()

pre_save.connect(dp_pre_save_reciever,sender=DonorProfile)

# post_save.connect(dp_post_save_reciever,sender=DonorProfile)
