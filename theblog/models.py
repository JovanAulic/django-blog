from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Category(models.Model):
	ime = models.CharField(max_length=100)

	def __str__(self):
		return self.ime

	def get_absolute_url(self):
		return reverse('home')

   

class Post(models.Model):
	naslov = models.CharField(max_length=260)
	broj_naslova = models.CharField(max_length=260)
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	tekst = RichTextField(blank=True, null=True)
	kategorija = models.CharField(max_length=200, default="coding")
	vanjski_tekst = models.CharField(max_length=200, default="Klikite Link Iznad da Pročitate Post...")

	def __str__(self):
		return self.naslov + '|' + str(self.autor)

	def get_absolute_url(self):
		return reverse('home')

  