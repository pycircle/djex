# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# https://docs.djangoproject.com/en/dev/ref/models/fields/

class Post(models.Model):
    author = models.ForeignKey(User, verbose_name="autor", null=True)
    posted = models.DateTimeField(verbose_name="opublikowano", auto_now_add=True)
    title = models.CharField(verbose_name=u"tytuł", max_length=50)
    text = models.TextField(verbose_name=u"treść")

    def __unicode__(self):
        return self.author.username + ":" + self.title