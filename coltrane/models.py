# -*- coding: utf-8 -*-
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=250, help_text="Maximum 250 caractères")
    slug = models.SlugField(unique=True, help_text="Valeur suggérée automatiquement à partir du titre. Doit être unique")
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = "categories"
        ordering = ["title"]
    
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/categories/%s/" % self.slug
