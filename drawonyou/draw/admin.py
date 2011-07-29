from django.contrib import admin
from drawonyou.draw.models import FacebookProfile
	
class FacebookProfileAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'gender', 'birthday', 'fbid')

admin.site.register(FacebookProfile, FacebookProfileAdmin)
