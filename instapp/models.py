from django.db import models
import datetime as dt
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    profile_photo= models.ImageField(upload_to='profiles/',null=True)
    bio= models.CharField(max_length=100, null=True)

    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls, user):
        profile = cls.objects.filter(user=user).first()
):
        followers = cls.objects.filter(user=user).all()
        return followers

    class Meta:
        ordering = ['user']
