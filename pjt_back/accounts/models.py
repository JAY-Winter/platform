from django.db import models
from django.contrib.auth.models import AbstractUser
from projects.models import Skill as Skill
from projects.models import Campus as Campus

class Part(models.Model):
    part = models.IntegerField()


class User(AbstractUser):
    campus = models.ForeignKey(Campus, blank=True, null=True, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, blank=True, null=True, on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skill, blank=True)
    github = models.CharField(max_length=300, blank=True, null=True)
    blog = models.CharField(max_length=300, blank=True, null=True)
    introduce = models.CharField(max_length=300, blank=True, null=True)
    followings = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='followers')