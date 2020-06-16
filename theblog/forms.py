from django import forms 
from .models import Post, Category

choices = Category.objects.all().values_list('ime','ime')
choice_list = []

for item in choices:
	choice_list.append(item)
	

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('naslov', 'broj_naslova', 'autor','kategorija', 'tekst','vanjski_tekst')

		widgets = {
		'naslov': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Napišite naslov!'}),
		'broj_naslova': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Napišite redni broj posta!'}),
		'autor': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'vase_ime', 'type':'hidden'}),
		#'autor': forms.Select(attrs={'class': 'form-control'}),
		'kategorija': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
		'tekst': forms.Textarea(attrs={'class': 'form-control'}),
		'vanjski_tekst' : forms.Textarea(attrs={'class': 'form-control'}),
			}

class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('naslov', 'broj_naslova', 'tekst','vanjski_tekst')

		widgets = {
		'naslov': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Napišite naslov!'}),
		'broj_naslova': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Napišite redni broj posta!'}),
		'tekst': forms.Textarea(attrs={'class': 'form-control'}),
		'vanjski_tekst' : forms.Textarea(attrs={'class': 'form-control'}),
			}
