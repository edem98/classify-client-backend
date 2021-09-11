from django.contrib import admin
from .models import ClassifiedUser, Cars
from django.utils.html import format_html

@admin.register(ClassifiedUser)
class ClassifiedUserAdmin(admin.ModelAdmin):
	list_filter = ['ever_married','graduated','anonymised_category','segmentation','gender']
	search_fields = ['first_name','last_name','profession']
	list_display = ('user','first_name','last_name',
		'email','gender','ever_married',
		'birth_day','graduated','profession',
		'work_experience', 'spending_score',
		'family_size', 'family_size', 'anonymised_category',
		'segmentation'
		)



@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
	list_display = ('brand','model','color','category','display_image')

	def display_image(self, obj):
		if obj.image != None:
			return format_html('<a href="{}" target= "_blank"> <img src="{}" width="150px"/> </a>',
							   obj.image.url, obj.image.url, )
		else:
			return format_html('No image available')